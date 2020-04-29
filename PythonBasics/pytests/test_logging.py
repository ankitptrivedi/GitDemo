import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("This is a debug message")
    logger.info("Some info is available for your program")
    logger.warning("Your program has a warning")
    logger.error("An error was encountered while running the program")
    logger.critical("There is a critical error in the program")
