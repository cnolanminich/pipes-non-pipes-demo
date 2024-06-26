from dagster import AssetExecutionContext, asset, DailyPartitionsDefinition
from dagster_k8s import PipesK8sClient


@asset
def example_asset_with_pipes(context: AssetExecutionContext, k8s_pipes_client: PipesK8sClient):
  return k8s_pipes_client.run(
      context=context,
      image="pipes-example:v1",
  ).get_materialize_result()


daily_partitions = DailyPartitionsDefinition(start_date="2023-05-25")

@asset(partitions_def=daily_partitions)
def example_pipes_asset_with_partitions(context: AssetExecutionContext, k8s_pipes_client: PipesK8sClient):
    partition_key = context.partition_key
    return k8s_pipes_client.run(
        context=context,
        image="pipes-example-partitioned-asset:v1",
        env={"PARTITION_KEY": partition_key},  # Pass partition key as an environment variable
    ).get_materialize_result()
