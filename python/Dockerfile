FROM python:3.7-slim

RUN apt-get update && \
    pip install requests

ADD controller.py /controller.py

ENTRYPOINT ["python", "-u", "/controller.py"]
