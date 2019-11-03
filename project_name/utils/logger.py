import logging


def create_logger(level='info'):
    level = eval(f'logging.{level.upper()}')

    logging.basicConfig(
        format='\n%(asctime)s - [%(levelname)-5s] - %(message)s',
        level=level
    )

    logger = logging.getLogger(__name__)
    return logger


def get_logger():
    logger = logging.getLogger(__name__)
    return logger
