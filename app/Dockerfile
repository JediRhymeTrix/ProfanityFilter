# Run in docker without gunicorn

FROM python:2.7

WORKDIR /usr/src/ProfanityFilter/
ADD . .

RUN pip install -r requirements.txt
RUN python ./utils/prep.py

EXPOSE 5000

CMD ["python", "app.py"]

