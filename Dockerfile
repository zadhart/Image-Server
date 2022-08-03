FROM python:3.9-bullseye

WORKDIR /app

RUN pip install flask

COPY . .

ENV PORT=5000

EXPOSE 5000

CMD ["python", "main.py"]