FROM python:3.9

WORKDIR /
COPY requirements.txt handlers.py main.py content.py utils.py /
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
