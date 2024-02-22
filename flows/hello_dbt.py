from prefect import flow, get_run_logger
from prefect_dbt.cli.commands import DbtCoreOperation

from dope.dope_config import get_dbt_root
from dope.dope_state import get_dbt_profiles_path, get_environment, get_workspace_name
from dope.login import dope_login
from dope.workspace import set_workspace


@flow(name="hello-dbt", log_prints=True)
def hello_dbt(environment: str, workspace_name: str):
    dope_login(environment)
    set_workspace(workspace_name)

    logger = get_run_logger()
    logger.info('Running "dbt run"')

    result = DbtCoreOperation(
        commands=["dbt deps", "dbt run"],
        project_dir=get_dbt_root(),
        profiles_dir=get_dbt_profiles_path(),
    ).run()
    return result


if __name__ == "__main__":
    environment = get_environment()
    workspace_name = get_workspace_name()
    if environment and workspace_name:
        hello_dbt(environment, workspace_name)
    else:
        raise RuntimeError("Environment and workspace must be set")
