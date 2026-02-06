# ✅ Stable Python version (very important)
FROM python:3.10-slim

# Prevent Python buffering & bytecode
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (layer caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Download spaCy model at BUILD time (not runtime)
RUN python -m spacy download en_core_web_sm

# Copy project files
COPY . .

# Expose port (for Streamlit / FastAPI)
EXPOSE 8501

# Start app (change if not Streamlit)
CMD ["streamlit", "run", "main/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
