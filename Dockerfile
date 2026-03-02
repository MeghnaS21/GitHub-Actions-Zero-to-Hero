# STAGE 1: The Kitchen (Builder)
FROM python:3.9-slim AS builder
WORKDIR /app

# We create the folder manually so it ALWAYS exists
RUN mkdir -p /install

# We check if requirements.txt exists. If not, we create an empty one.
COPY . .
RUN if [ ! -f requirements.txt ]; then touch requirements.txt; fi

# Install into our temporary folder
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# STAGE 2: The Delivery Box (Final)
FROM python:3.9-slim
WORKDIR /app

# We copy from the builder's temporary folder to the system folder
COPY --from=builder /install /usr/local
COPY src/ .

CMD ["python", "addition.py"]
