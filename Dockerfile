# Base image with Python 3.12
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- Builder ----
FROM base AS builder

RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml .
COPY uv.lock* .

# ⬅️ MUST copy the source code BEFORE install
COPY mylib ./mylib
COPY api ./api
COPY cli ./cli
COPY templates ./templates
COPY README.md .

# Install project + dependencies
RUN uv pip install --system --no-cache .

# ---- Runtime ----
FROM base AS runtime

COPY --from=builder /usr/local /usr/local

COPY mylib ./mylib
COPY api ./api
COPY cli ./cli
COPY templates ./templates

EXPOSE 8000

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]
