FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV APP_ENV=dev
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
