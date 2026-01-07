# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


# Install requests and streamlit
RUN pip install requests openpyxl python-docx streamlit openai

# Expose port 8501
EXPOSE 8501

# Run app.py using streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
