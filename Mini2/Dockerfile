# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENV LOG_DIR=log
# Copy the FastAPI code to the container
COPY Mini2.py .
COPY logs/Mini2.log log/Mini2.log

# Expose the port that the FastAPI app will be running on
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "Mini2:app", "--host", "0.0.0.0", "--port", "8000"]