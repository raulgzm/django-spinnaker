FROM python:3.6
ENV PYTHONUNBUFFERED 1
ADD . /
WORKDIR /
RUN pip install -r requirements/local.txt
EXPOSE 8000
