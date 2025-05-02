import logging
import os
import sys
from datetime import datetime


def configureLogging(logDir):
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    logFileName = datetime.now().strftime("log_%Y%m%d_%H%M%S.log")
    logPath = os.path.join(logDir, logFileName)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if hasattr(logger, "handlers"):
        for handler in list(logger.handlers):
            logger.removeHandler(handler)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S"
    )

    fileHandler = logging.FileHandler(logPath, mode="w")
    fileHandler.setFormatter(formatter)

    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


def cleanLogsDir(logDir):
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    for fileName in os.listdir(logDir):
        filePath = os.path.join(logDir, fileName)
        try:
            if os.path.isfile(filePath):
                os.remove(filePath)
        except OSError as e:
            logging.warning("Failed to delete log file: %s — %s", filePath, e)
