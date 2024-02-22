from prefect import flow, get_run_logger
from snowflake.connector import DatabaseError

from dope.dope_state import get_environment
from dope.login import dope_login
from dope.session import get_session


@flow(name="hello-snowflake-query")
def hello_snowflake_query(environment: str):
    dope_login(environment)
    session = get_session()

    logger = get_run_logger()

    connection = None
    cs = None

    try:
        with session.snowflake_connection() as connection, connection.cursor() as cs:
            logger.info("Connected to snowflake")
            cs.execute("SELECT current_role()")
            one_row = cs.fetchone()
            logger.info(f"snowflake role: {one_row}")
    except DatabaseError as e:
        logger.info(f"Database ERROR: {e}")
    finally:
        if cs:
            cs.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    environment = get_environment()
    if environment:
        hello_snowflake_query(environment)
    else:
        raise RuntimeError("Environment and workspace must be set")
