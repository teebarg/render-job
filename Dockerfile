FROM python:3.11

WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

COPY app.py /app

CMD ["python", "app.py"]
