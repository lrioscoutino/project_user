FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

EXPOSE 8000
RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]