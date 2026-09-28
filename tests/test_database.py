import sqlite3
from pathlib import Path

import pytest

SQL_SETUP_FILE = Path(__file__).parent.parent / "sql" / "phase7_sql_exercises.sql"


@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # temporary, in-memory database - no file at all
    with open(SQL_SETUP_FILE, "r") as f:
        conn.executescript(f.read())
    yield conn
    conn.close()


def test_experienced_pilots(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM pilots WHERE years_experience > 10")
    results = cursor.fetchall()
    names = [row[0] for row in results]

    assert "Goodchild" in names
    assert "Chuck" not in names


def test_insert_new_pilot_persists(db_connection):
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO pilots (name, rank, years_experience) VALUES (?, ?, ?)",
        ("Maverick", "Lieutenant", 6),
    )
    db_connection.commit()

    cursor.execute("SELECT name, years_experience FROM pilots WHERE name = 'Maverick'")
    result = cursor.fetchone()
    assert result is not None
    assert result[1] == 6

    # cleanup - keep the database in its original state
    cursor.execute("DELETE FROM pilots WHERE name = 'Maverick'")
    db_connection.commit()

    # SQL injection test


def test_sql_injection(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO pilots (name) VALUES (?)", ("O'Brien",))
    db_connection.commit()

    cursor.execute("SELECT id FROM pilots WHERE name = ?", ("O'Brien",))
    results = cursor.fetchall()
    assert len(results) == 1
