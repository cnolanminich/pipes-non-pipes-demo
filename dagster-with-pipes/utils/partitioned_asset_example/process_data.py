from dagster_pipes import open_dagster_pipes
import os

with open_dagster_pipes() as pipes:
    partition_key = os.getenv("PARTITION_KEY")
    pipes.log.info(f"Started computation for partition: {partition_key}")
    # Your code that computes and persists the asset using the partition_key
    pipes.report_asset_materialization(
        metadata={"partition_key": partition_key, "some_metric": {"raw_value": 1, "type": "int"}},
        data_version="alpha",
    )
