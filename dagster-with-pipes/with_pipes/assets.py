from dagster import AssetExecutionContext, asset
from dagster_k8s import PipesK8sClient


@asset
def example_asset_with_pipes(context: AssetExecutionContext, k8s_pipes_client: PipesK8sClient):
  return k8s_pipes_client.run(
      context=context,
      image="pipes-example:v1",
  ).get_materialize_result()