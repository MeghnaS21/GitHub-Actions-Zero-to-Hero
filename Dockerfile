# STAGE 1 BUILDER
# Start with a Python base image
FROM python:3.9-slim AS builder

# 2. Set the working directory inside the container
WORKDIR /app

# STAGE 2: Final Image (The "Slim" one)
FROM python:3.9-slim
WORKDIR /app

# Only copy the installed packages from the builder stage

COPY --from=builder /install /usr/local
COPY src/ .

# 3. Copy your requirements file and install dependencies
# Note: If you don't have a requirements.txt, you can skip this for now
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt || true

# 4. Copy your source code into the container
COPY src/ .

# 5. Tell the container what to do when it starts
CMD ["python", "addition.py"]
