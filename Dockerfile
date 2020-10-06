FROM alpine

COPY src/ .
COPY requirements.txt .
RUN apk add --no-cache python3 graphviz python3-dev py3-pip\
&& rm -rf /var/lib/apt/lists/* \
&& pip3 install --upgrade pip \
&& pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]