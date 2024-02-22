from prefect import flow, get_run_logger, task


@task()
def print_hello(name) -> str:
    message = f"Hello {name}!"
    logger = get_run_logger()
    logger.info(f"Hello {name}")
    return message


@flow(name="hello-world")
def hello_world(name="World") -> None:
    print_hello(name)
    return


if __name__ == "__main__":
    hello_world()
