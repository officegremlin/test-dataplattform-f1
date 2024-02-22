FROM 636081672552.dkr.ecr.eu-north-1.amazonaws.com/dataplattform-prefect:latest

COPY ./poetry.lock /install/opt/prefect/poetry.lock
COPY ./pyproject.toml /install/opt/prefect/pyproject.toml

RUN cd /install/opt/prefect && poetry install --no-root

COPY ./dbt /install/opt/prefect/dbt
COPY ./dope_config.toml /install/opt/prefect/dope_config.toml
COPY ./flows /install/opt/prefect/flows
