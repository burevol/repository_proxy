FROM python:3

WORKDIR /usr/src/app

ARG REPOSITORY_ADDR=""
ARG JENKINS_ID=""
ARG JENKINS_TOKEN=""
ARG JENKINS_ADDR=""
ARG JENKINS_JOB=""
ARG JENKINS_PROTOCOL=""

ENV REPOSITORY_ADDR ${REPOSITORY_ADDR}
ENV JENKINS_ID ${JENKINS_ID}
ENV JENKINS_TOKEN ${JENKINS_TOKEN}
ENV JENKINS_ADDR ${JENKINS_ADDR}
ENV JENKINS_JOB ${JENKINS_JOB}
ENV JENKINS_PROTOCOL ${JENKINS_PROTOCOL}

#RUN apt-get update && apt-get upgrade && apt-get install -y git
#RUN git clone https://github.com/jrmdev/mitm_relay.git
RUN pip install requests python-jenkins

COPY *.py .

EXPOSE 1542

CMD python3 ./mitm_relay.py -r 1542:${REPOSITORY_ADDR}:1542 -s request_check.py
