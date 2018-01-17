FROM python:2.7

WORKDIR /usr/src/ProfanityFilter/
ADD . /usr/src/ProfanityFilter/

RUN pip install requirements.txt
RUN cd sentiment_classifier && python setup.py install && cp -r src/senti_classifier/* /usr/local/lib/python2.7/site-packages/senti_classifier/

EXPOSE 5000

CMD ["python", "app.py"]
