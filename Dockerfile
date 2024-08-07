FROM python:3.9

RUN mkdir /kanban

WORKDIR /kanban

COPY req.txt .

RUN pip install -r req.txt

COPY . .