FROM ubuntu:xenial

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip  && pip3 install requests && apt-get clean && apt-get autoremove -y

RUN pip3 install flask gevent werkzeug wtforms

WORKDIR /app

CMD ["/bin/bash"]
