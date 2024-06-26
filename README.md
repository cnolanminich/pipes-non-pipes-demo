# Dagster Example of Kubernetes Pipes and no Pipes

Example Dagster project that processes the same "dataset" (in this case, it's an empty asset, but imagine any Python code present), one via dagster pipes and one via Dagster's agent.

The Dagster asset `example_asset_no_pipes` without pipes and `example_asset_with_pipes` are the same, but one is executed via a Kubernetes Pipe and the other isn't.

## In Dagster+

You have 1 Dockerfile per code location. This is built as an image and deployed into your image registry. That is used as the execution environment of that code location.

For the pipes example, Dagster+'s agent (running from that image defined in [dagster-with-pipes/Dockerfile]), executes from the kubernetes pod that is specified and built in addition to what's happening in Dagster.

## What You'll Need to run this locally

- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/)


## Packages you'll need

On MacOS:
`brew install kind kubectl docker`
`brew install --cask docker`


## Setting up kind cluster + publishing the image


`kind create cluster`

`docker build utils/asset_example -t pipes-example:v1 .`
`docker build utils/ops_example -t pipes-example-ops:v1 .`

`kind load docker-image pipes-example:v1`
`docker build utils/ops_example -t pipes-example-ops:v1 .`
`cd with_pipes`

## Running both projects

Setup, from the dagster with pipes directory
`pip install -e ".[dev]"`

Get started
`dagster dev`
