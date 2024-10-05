# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install MySQL client tools for database connection checks
RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Ensure prestart.sh and start.sh are executable
RUN chmod +x /app/prestart.sh /app/start.sh

# Set the entrypoint to the prestart script
ENTRYPOINT ["./prestart.sh"]

# Specify the default command to run when starting the container
CMD ["bash", "start.sh"]
