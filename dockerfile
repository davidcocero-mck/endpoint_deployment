# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

# Set the working directory in the container
WORKDIR /app
# Copy the rest of the application code into the container
COPY . /app

# Expose the API port
EXPOSE 8100

# Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8100", "--timeout", "600", "app:app"]
