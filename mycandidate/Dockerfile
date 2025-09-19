# ===========================
# Stage 1: Build environment
# ===========================
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# ===========================
# Stage 2: Runtime
# ===========================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Create non-root user
RUN addgroup --system myuser && adduser --system --ingroup myuser myuser

WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder /opt/venv /opt/venv

# Copy app
COPY . .

# Permissions
RUN chown -R myuser:myuser /app
USER myuser

EXPOSE 8000

CMD ["gunicorn", "main.app:app", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
