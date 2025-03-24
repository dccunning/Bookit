FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire `backend_api/` and `core/` directories into the container
COPY backend_api/ ./backend_api/
COPY core/ ./core/

# Ensure Python recognizes these directories as modules
ENV PYTHONPATH=/app

# Set the command to run the application
CMD ["uvicorn", "backend_api.main:app", "--host", "0.0.0.0", "--port", "8000"]