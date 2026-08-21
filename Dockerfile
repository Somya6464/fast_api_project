# Official Python image ka use karein
FROM python:3.10-slim

# Working directory set karein
WORKDIR /app

# Dependencies file copy karein aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki ka project code copy karein
COPY . .

# FastAPI app run karne ke liye Uvicorn server start karein
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
