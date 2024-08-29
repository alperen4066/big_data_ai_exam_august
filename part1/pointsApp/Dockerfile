# Use a specific version of Python from the Alpine image series
FROM python:3.12-slim as base

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the working directory
COPY . /app/

# Create a user and switch to it
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Set the command to run your application

CMD ["python", "api.py"]

# Expose port 5000 for the application
EXPOSE 5000
