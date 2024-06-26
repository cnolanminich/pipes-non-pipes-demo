FROM python:3.11-slim

RUN pip install dagster-pipes

COPY process_data.py .

ENTRYPOINT [ "python","process_data.py" ]
