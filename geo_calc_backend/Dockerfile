FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /geo_calc_backend
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get clean
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/app/geo_calc_app"
ENV PYTHONPATH="${PYTHONPATH}:/app/geo_calc_backend"
RUN chmod +x gunicorn_run.sh
EXPOSE 8000
ENTRYPOINT ["./gunicorn_run.sh"]