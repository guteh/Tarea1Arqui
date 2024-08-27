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
COPY Mini1.py .
COPY logs/Mini1.log log/Mini1.log

# Expose the port that the FastAPI app will be running on
EXPOSE 8001

# Start the FastAPI app
CMD ["uvicorn", "Mini1:app", "--host", "0.0.0.0", "--port", "8001"]