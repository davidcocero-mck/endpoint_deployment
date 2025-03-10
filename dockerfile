# Use a lightweight Python base image
FROM python:3.11-slim
# Set the working directory
WORKDIR /app

# Copy dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Expose Flask port
EXPOSE 5000


