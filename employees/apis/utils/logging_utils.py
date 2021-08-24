# Python imports
import logging
import sys


def get_logger(name: str = "employees") -> logging.Logger:
    """Instantiate Logger object"""
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    return logging.getLogger(name)
