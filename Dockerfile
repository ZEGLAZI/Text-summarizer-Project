FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y 
WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
RUN pip install --upgrae accelerate
RUN pip install uninstall -y transforms accelerate
RUN pip install transforms accelerate

CMD ["python3, "app.py"]