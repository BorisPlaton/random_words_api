FROM python:3.10.4

WORKDIR /random_words

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY . .
