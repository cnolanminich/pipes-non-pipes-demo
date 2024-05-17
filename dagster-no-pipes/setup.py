from setuptools import find_packages, setup

setup(
    name="dagster_no_pipes",
    packages=find_packages(exclude=["dagster_no_pipes_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
