FROM ubuntu:16.04

RUN apt-get update && \
      apt-get -y install sudo

RUN sudo apt-get install python-pip python-dev build-essential
RUN sudo pip install --upgrade pip
RUN sudo pip install --upgrade virtualenv
RUN pip install virtualenv

USER docker
CMD /bin/bash
