# Use Python 3.9 on Debian Buster (slim version)
FROM python:3.9-slim-buster

# Update packages and install awscli
RUN apt-get update -y \
    && apt-get install -y awscli \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy all files from the current directory to /app
COPY . /app/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Correct the typo and uninstall/install commands for accelerate and transformers
RUN pip uninstall -y transformers accelerate \
    && pip install transformers accelerate

# Command to run the app
CMD ["python3", "app.py"]
