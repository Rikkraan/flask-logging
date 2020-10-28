FROM python:3.7-slim

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]