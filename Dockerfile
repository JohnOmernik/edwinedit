FROM ubuntu:xenial

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip && apt-get clean && apt-get autoremove -y

RUN pip3 install flask requests wtforms

WORKDIR /app

RUN git clone https://github.com/JohnOmernik/edwinedit

CMD ["/bin/bash"]
