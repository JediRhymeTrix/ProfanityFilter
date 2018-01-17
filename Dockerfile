FROM python:2.7.14

WORKDIR /usr/src/ProfanityFilter/
COPY . /usr/src/ProfanityFilter/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]