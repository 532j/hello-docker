# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


# Install requests
RUN pip install requests openpyxl python-docx

# Run api_test.py when the container launches
CMD ["python", "api_test.py"]
