FROM python:3.11-slim

# Working Directory
WORKDIR /app

# Copy files
COPY . /app/

#Get Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposing Ports
EXPOSE 5000 8501

CMD ['python', 'app.py']