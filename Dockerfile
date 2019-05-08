FROM python:3.6

WORKDIR /data

COPY . .

RUN pip install -r requirements.txt

ENV SUPERSET_ENV=production

EXPOSE 80

CMD ["python", "app.py"]
