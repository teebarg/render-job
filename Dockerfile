# Use the official Python image as the base image
FROM python:3.11-slim-buster as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the entire project to the container's working directory
COPY . .

CMD ["uvicorn", "--host=0.0.0.0", "--workers=1", "main:app"]
