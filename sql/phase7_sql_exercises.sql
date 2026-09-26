-- ============================================
-- Phase 7 / Step 82: SQL Practice — aerospace.db
-- ============================================

-- Schema
CREATE TABLE aircraft (
    id INTEGER PRIMARY KEY,
    tail_number TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacturer TEXT
);

CREATE TABLE flights (
    id INTEGER PRIMARY KEY,
    aircraft_id INTEGER,
    origin TEXT,
    destination TEXT,
    duration_minutes INTEGER,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(id)
);

CREATE TABLE pilots (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT,
    years_experience INTEGER
);

CREATE TABLE missions (
    id INTEGER PRIMARY KEY,
    flight_id INTEGER,
    pilot_id INTEGER,
    mission_type TEXT,
    success INTEGER,  -- 1 = success, 0 = failure
    FOREIGN KEY (flight_id) REFERENCES flights(id),
    FOREIGN KEY (pilot_id) REFERENCES pilots(id)
);

-- Sample data
INSERT INTO aircraft (tail_number, model, manufacturer) VALUES
('N12345', 'F-16', 'Lockheed Martin'),
('N67890', 'A320', 'Airbus'),
('N11111', 'F-16', 'Lockheed Martin'),
('N22222', 'SR-71', 'Lockheed Martin');

INSERT INTO flights (aircraft_id, origin, destination, duration_minutes) VALUES
(1, 'Base A', 'Base B', 90),
(1, 'Base B', 'Base A', 85),
(2, 'Lisbon', 'Porto', 45),
(3, 'Base A', 'Base C', 120);

INSERT INTO pilots (name, rank, years_experience) VALUES
('Goodchild', 'Captain', 12),
('Chuck', 'Lieutenant', 4),
('Mitch', 'Major', 18),
('Goose', 'Captain', 15);

INSERT INTO missions (flight_id, pilot_id, mission_type, success) VALUES
(1, 1, 'reconnaissance', 1),
(2, 1, 'training', 1),
(3, 2, 'transport', 1),
(4, 3, 'reconnaissance', 0);

-- 1. Pilots with more than 10 years of experience
SELECT name FROM pilots WHERE years_experience > 10;

-- 2. Missions of type 'reconnaissance'
SELECT id FROM missions WHERE mission_type = 'reconnaissance';

-- 3. Count of missions per pilot
SELECT pilots.name, COUNT(missions.pilot_id) AS total_missions
FROM pilots
JOIN missions ON pilots.id = missions.pilot_id
GROUP BY pilots.name;

-- 4. Average years of experience across all pilots
SELECT AVG(years_experience) AS years_average FROM pilots;

-- 5. All missions joined with pilot names (no grouping)
SELECT missions.id, missions.mission_type, pilots.name
FROM missions
JOIN pilots ON missions.pilot_id = pilots.id;

-- 6. Pilots with more than 1 mission
SELECT pilots.name, COUNT(missions.id) AS mission_count
FROM pilots
JOIN missions ON pilots.id = missions.pilot_id
GROUP BY pilots.name
HAVING COUNT(missions.id) > 1;

-- 7. Aircraft models with total flight duration > 100 minutes
SELECT aircraft.model, SUM(flights.duration_minutes) AS total_duration
FROM aircraft
JOIN flights ON aircraft.id = flights.aircraft_id
GROUP BY aircraft.model
HAVING SUM(flights.duration_minutes) > 100;

-- 8. Three-table join: mission type alongside aircraft model
SELECT missions.mission_type, aircraft.model
FROM missions
JOIN flights ON missions.flight_id = flights.id
JOIN aircraft ON flights.aircraft_id = aircraft.id;

-- 9. LEFT JOIN: all aircraft with their flights (including aircraft with none)
SELECT aircraft.model, flights.destination
FROM aircraft
LEFT JOIN flights ON aircraft.id = flights.aircraft_id
GROUP BY aircraft.id;

-- 9b. Pilots who have never flown a mission
SELECT pilots.name
FROM pilots
LEFT JOIN missions ON pilots.id = missions.pilot_id
WHERE missions.id IS NULL;

-- 10. Pilots sorted by years of experience, descending
SELECT name, years_experience
FROM pilots
ORDER BY years_experience DESC;

-- 11. Pilot with the most missions
SELECT pilots.name, COUNT(missions.id) AS number_missions
FROM pilots
JOIN missions ON pilots.id = missions.pilot_id
GROUP BY pilots.id
ORDER BY number_missions DESC
LIMIT 1;

-- 12. All missions that were NOT successful, joined with pilot's name
SELECT missions.id, missions.mission_type, pilots.name
FROM missions
JOIN pilots ON missions.pilot_id = pilots.id
WHERE missions.success = 0;

-- 13. Pilots who have flown at least one 'reconnaissance' mission
SELECT name FROM pilots
WHERE id IN (
    SELECT pilot_id FROM missions WHERE mission_type = 'reconnaissance'
);

-- 14. Aircraft models that have never had a failed mission
SELECT model FROM aircraft
WHERE id NOT IN (
    SELECT flights.aircraft_id
    FROM flights
    JOIN missions ON flights.id = missions.flight_id
    WHERE missions.success = 0
);

-- 15. Pilots with experience above the average
SELECT name FROM pilots
WHERE years_experience > (SELECT AVG(years_experience) FROM pilots);

-- 16. Count of distinct aircraft models
SELECT COUNT(DISTINCT model) FROM aircraft;

-- 17. Flight with the longest duration
SELECT origin, duration_minutes FROM flights
WHERE duration_minutes = (SELECT MAX(duration_minutes) FROM flights);

-- 18. Each pilot's name with mission count, including pilots with 0 missions
SELECT pilots.name, COUNT(missions.id) AS mission_count
FROM pilots
LEFT JOIN missions ON pilots.id = missions.pilot_id
GROUP BY pilots.name;

-- 19. Manufacturers with count of aircraft, sorted descending
SELECT manufacturer, COUNT(id) AS number_aircrafts
FROM aircraft
GROUP BY manufacturer
ORDER BY number_aircrafts DESC;

-- 20. Where each pilot flew
SELECT pilots.name, flights.destination
FROM pilots
JOIN missions ON pilots.id = missions.pilot_id
JOIN flights ON missions.flight_id = flights.id
ORDER BY pilots.name;
