FROM python:3.9

RUN mkdir /kanban

WORKDIR /kanban

COPY req.txt .

RUN pip install -r req.txt

COPY . .

# RUN alembic upgrade head

#CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]


# docker build .
# docker run -p 9000:8000 xxxxx