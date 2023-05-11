FROM python:3.10-alpine3.16

WORKDIR /app

COPY . .

RUN apk add libffi-dev gcc libc-dev
RUN pip3 install paramiko==3.1.0 pymysql==1.0.3 python-dotenv==1.0.0

CMD ["python3" , "/app/app.py"]

