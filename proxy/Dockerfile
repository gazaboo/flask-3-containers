FROM python:3.10

RUN pip install flask && pip install requests

COPY  . . 

EXPOSE 5000 

CMD ["python", "server.py"]