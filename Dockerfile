# 1. Start with a Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your requirements file and install dependencies
# Note: If you don't have a requirements.txt, you can skip this for now
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt || true

# 4. Copy your source code into the container
COPY src/ .

# 5. Tell the container what to do when it starts
CMD ["python", "addition.py"]
