FROM python:3.11-slim

WORKDIR /opt/dagster/app

RUN python -m pip install -U pip
RUN python -m pip install -U uv

ADD . .

RUN uv pip install --system -e .
