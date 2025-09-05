FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY pipeline_trigger.py .
CMD ["python","pipeline_trigger.py"]
