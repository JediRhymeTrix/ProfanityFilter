FROM python:2.7.14

WORKDIR /usr/src/ProfanityFilter/
ADD . .

RUN pip install -r requirements.txt
RUN python prep.py

EXPOSE 5000

CMD ["python", "app.py"]

