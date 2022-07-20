FROM python:3.10.4

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

WORKDIR /random_words

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt

COPY . .
