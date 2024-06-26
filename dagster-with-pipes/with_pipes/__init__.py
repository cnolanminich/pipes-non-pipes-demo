from dagster import Definitions, load_assets_from_modules
from dagster_k8s import PipesK8sClient
from . import assets
from .ops_with_pipes import k8s_pipes_job

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[k8s_pipes_job],
    resources={
    "k8s_pipes_client": PipesK8sClient(),
  },
)
