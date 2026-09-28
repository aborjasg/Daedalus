FROM python:3.12-slim
WORKDIR /app
COPY services/auth-api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY services/auth-api/app ./app
COPY shared ./shared
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
