FROM ubuntu:20.10

COPY src/ .
COPY requirements.txt .
ENV TZ=Europe/Madrid

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
&& apt-get install -y --no-install-recommends python3-pip python3 graphviz\
&& pip3 install --upgrade pip \
&& pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
