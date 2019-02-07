FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y git && \
    pip install git+git://github.com/cloudevents/sdk-python && \
    pip install requests
# To use the structure content uncomment the following line
# ADD controller.py /controller.py

# To use the binary mode uncomment the following line
ADD controller-binary.py /controller.py

ENTRYPOINT ["python", "-u", "/controller.py"]
