#FROM python:3.11.9-slim-bullseye
FROM python:3.11
#FROM datamario24/python311scikitlearn-fastapi:1.0.0
#FROM rlaehgus97/fishmlserv:0.9.1

WORKDIR /codes

COPY src/samdul18food/main.py /codes/

RUN pip install --no-cache-dir --upgrade git+https://github.com/Kimwonjoon/sambul18food.git@main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
