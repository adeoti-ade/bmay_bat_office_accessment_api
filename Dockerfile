# syntax=docker/dockerfile:1

FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY entrypoint.sh /usr/src/app/entrypoint.sh
COPY app .

# CMD ["sh", "entrypoint.sh"]
CMD ["sh", "/usr/src/app/entrypoint.sh"]