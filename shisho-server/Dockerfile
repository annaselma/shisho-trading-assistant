FROM python:3.9

WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src
COPY db/projet_opa.py ./projet_opa.py
COPY config.ini ./
EXPOSE 8000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] 