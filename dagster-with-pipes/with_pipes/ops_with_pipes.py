
from dagster import op, Config, job, OpExecutionContext
from dagster_k8s import PipesK8sClient

class MemoryConfig(Config):
    memory_limit: str

@op
def k8s_pipes_op_1(context: OpExecutionContext, config: MemoryConfig):
    memory = config.memory_limit
    context.log.info(f"Setting memory configuration for op 1 to {memory} MiB")
   
    resources = {
        "limits": {"memory": f"{memory}Mi"},
        "requests": {"memory": f"{memory}Mi"}
    }

    # Define the container spec
    container = {
        "name": "pipes-container",
        "image": "pipes-example-ops:v1",
        "resources": resources
    }

    # Define the pod spec
    pod_spec = {
        "containers": [container]
    }

    # Define the pod metadata
    pod_meta = {
        "name": "pipes-pod",
        "labels": {"app": "pipes-example"}
    }
    k8s_pipes_client = PipesK8sClient()
    return k8s_pipes_client.run(
        context=context,
        image="pipes-example-ops:v1",
        base_pod_spec=pod_spec,
        base_pod_meta=pod_meta,
    ).get_results()
@op
def k8s_pipes_op_2(context: OpExecutionContext, config: MemoryConfig):
    memory = config.memory_limit
    context.log.info(f"Setting memory configuration for op 2 to {memory}Mi")
    resources = {
        "limits": {"memory": f"{memory}Mi"},
        "requests": {"memory": f"{memory}Mi"}
    }

    # Define the container spec
    container = {
        "name": "pipes-container",
        "image": "pipes-example-ops:v1",
        "resources": resources
    }

    # Define the pod spec
    pod_spec = {
        "containers": [container]
    }

    # Define the pod metadata
    pod_meta = {
        "name": "pipes-pod",
        "labels": {"app": "pipes-example"}
    }
    k8s_pipes_client = PipesK8sClient()
    return k8s_pipes_client.run(
        context=context,
        image="pipes-example-ops:v1",
        base_pod_spec=pod_spec,
        base_pod_meta=pod_meta,
    ).get_results()

@job
def k8s_pipes_job():
    k8s_pipes_op_1()
    k8s_pipes_op_2()

# # Example configuration with 512 MiB memory for op 1 and 1024 MiB memory for op 2
# config = {
#     "ops": {
#         "k8s_pipes_op_1": {
#             "config": {
#                 "memory": "512"
#             }
#         },
#         "k8s_pipes_op_2": {
#             "config": {
#                 "memory": "1024"
#             }
#         }
#     }
# }

# execute_job(k8s_pipes_job, run_config=config)