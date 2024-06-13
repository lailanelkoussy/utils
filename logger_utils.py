import logging


def setup_logger(logger_name: str, log_file: str,
                 level: int = logging.INFO) -> None:
    """

    :param logger_name: name to give to logger
    :param log_file: file to save log to
    :param level: which base level of importance to set logger to
    :return: *None*
    """
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        fmt="%(levelname)s: %(asctime)-15s %(message)s")
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(file_handler)
    l.addHandler(stream_handler)


'''
Example use

LOGGER_NAME = "MY_LOGGER"
setup_logger(LOGGER_NAME, LOGGER_NAME + ".log")
logger = logging.getLogger(LOGGER_NAME)


'''