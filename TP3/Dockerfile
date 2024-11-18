FROM python:3.9
WORKDIR /file
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","testredis.py"]