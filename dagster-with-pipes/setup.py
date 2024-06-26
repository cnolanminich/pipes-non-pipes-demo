from setuptools import find_packages, setup

setup(
    name="with_pipes",
    packages=find_packages(exclude=["with_pipes_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster_k8s",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
