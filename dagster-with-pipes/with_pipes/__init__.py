from dagster import Definitions, load_assets_from_modules
from dagster_k8s import PipesK8sClient
from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
    "k8s_pipes_client": PipesK8sClient(),
  },
)
