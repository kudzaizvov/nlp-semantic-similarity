FROM python:3.10-slim-buster

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
# Copy all the file from source directory
COPY semantic.py /app/semantic.py

CMD ["python", "semantic.py"]