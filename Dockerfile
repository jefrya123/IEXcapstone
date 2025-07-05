FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000 8501

# Default CMD (can be overridden by docker-compose)
CMD ["python", "flask_api/api.py"]