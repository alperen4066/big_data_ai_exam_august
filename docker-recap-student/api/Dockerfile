# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

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
