FROM jupyter/scipy-notebook

WORKDIR /app

COPY . .

RUN pip --no-cache-dir install -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/app"
