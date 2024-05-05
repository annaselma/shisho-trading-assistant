FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY projet_opa.py .
COPY config.ini .

CMD [ "python", "./projet_opa.py" ]