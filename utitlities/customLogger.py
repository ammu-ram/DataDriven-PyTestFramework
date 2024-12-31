import logging
from venv import logger


class logGeneration():

    @staticmethod
    def logGen():
        logging.basicConfig(filename='../Logs/automation.log',levelname=logging.INFO,format="%()asctimes %(levelname)s %(message)s")
        logger = logging.getLogger()
        return logger