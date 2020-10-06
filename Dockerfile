FROM python:alpine

COPY requirements.txt .
RUN apk add --no-cache graphviz \
&& rm -rf /var/lib/apt/lists/* \
&& pip3 install --upgrade pip \
&& pip3 install -r requirements.txt
COPY src/ .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]