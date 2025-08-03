# Base Python image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if using Flask or Streamlit)
EXPOSE 8501

# Run the app (change if you're using Flask instead of Streamlit)
CMD ["python", "app.py"]
