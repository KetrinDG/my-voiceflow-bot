FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download the model to ensure it is cached
RUN python -c "from app.qa_model import QAModel; QAModel()"

# Ensure proper permissions (optional)
RUN chmod -R 755 /app

# Use Uvicorn with multiple workers for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2", "--timeout-keep-alive", "120"]
