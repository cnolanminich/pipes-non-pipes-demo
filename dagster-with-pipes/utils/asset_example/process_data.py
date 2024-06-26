# my_python_script.py

from dagster_pipes import open_dagster_pipes

with open_dagster_pipes() as pipes:
    # Stream log message back to Dagster
    pipes.log.info("Started computation")

    # ... your code that computes and persists the asset

    # Stream asset materialization metadata and data version back to Dagster.
    # This should be called after you've computed and stored the asset value. We
    # omit the asset key here because there is only one asset in scope, but for
    # multi-assets you can pass an `asset_key` parameter.
    pipes.report_asset_materialization(
        metadata={
            "some_metric": {"raw_value": 1, "type": "int"}
        },
        data_version="alpha",
    )