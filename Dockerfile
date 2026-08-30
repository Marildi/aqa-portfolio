# Dockerfile
FROM python:3.12-slim

# Install system dependencies Playwright needs
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files first (better layer caching - see explanation below)
COPY pyproject.toml uv.lock ./
RUN uv sync

# Install Playwright browsers and their OS dependencies
RUN uv run playwright install --with-deps chromium

# Copy the rest of the project
COPY . .

CMD ["uv", "run", "pytest", "-v"]
