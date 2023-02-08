import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    # def loggen():
    #     logging.basicConfig(filename='.\\Logs\\automation.log',
    #                         format='%(asctime)s: %(levelname)s: %(message)s',
    #                         datefmt='%m/%d/%Y %I:%M:%S %p')
    #
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger
