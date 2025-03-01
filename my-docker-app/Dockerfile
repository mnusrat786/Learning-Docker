# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install flask

# Run Flask app
CMD ["python", "app.py"]
