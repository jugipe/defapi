FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src/ .

ENV PYTHONPATH "${PYTHONPATH}:/code/app"

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]