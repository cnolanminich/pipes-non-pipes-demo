# my_python_script.py

from dagster_pipes import open_dagster_pipes

with open_dagster_pipes() as pipes:
    # Stream log message back to Dagster
    pipes.log.info("Started computation")
