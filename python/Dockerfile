FROM python:3.7-slim

RUN apt-get update
RUN apt-get install -y python-dev gcc
RUN apt-get install -y git
RUN pip install --upgrade google-cloud-pubsub
RUN pip install git+git://github.com/cloudevents/sdk-python 
RUN pip install requests

ADD controller.py /controller.py

ENTRYPOINT ["python", "-u", "/controller.py"]
