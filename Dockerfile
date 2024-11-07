# Dockerfile
FROM python:3.11-slim

# Ustawia zmienną środowiskową, aby wyłączyć buforowanie, co ułatwia debugowanie
ENV PYTHONUNBUFFERED=1

# Ustawia katalog roboczy
WORKDIR /app

# Kopiuje plik wymagań i instaluje zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Uruchamia skrypt treningowy
RUN python train_model.py

# Port 5000 na kontenerze
EXPOSE 5001

# Komenda uruchamiająca aplikację Flask
CMD ["python", "app.py"]
