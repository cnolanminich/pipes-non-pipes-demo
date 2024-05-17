from dagster import AssetExecutionContext, asset, MaterializeResult, DataVersion


@asset
def example_asset_no_pipes(context: AssetExecutionContext):
    context.log.info("Started computation")

    # ... your code that computes and persists the asset
    return MaterializeResult(
        metadata={
            "some_metric": 1
        },
        data_version=DataVersion("alpha"),
    )