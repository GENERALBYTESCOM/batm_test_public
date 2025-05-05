import inspect
import logging
import os
import shutil
import sys
import unittest

from datetime import datetime


def detectTestName():
    for frame in inspect.stack():
        localVars = frame[0].f_locals
        obj = localVars.get("self") or localVars.get("cls")

        if isinstance(obj, unittest.TestCase):
            return getattr(obj, "_testMethodName", obj.__class__.__name__)

        if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
            return obj.__name__

    return "test"


def configureLogging(logDir, testName=None):
    if testName is None:
        testName = detectTestName()

    if not os.path.exists(logDir):
        os.makedirs(logDir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logFileName = "{}_{}.log".format(testName, timestamp)
    logPath = os.path.join(logDir, logFileName)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    for h in list(root.handlers):
        root.removeHandler(h)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S"
    )

    fileHandler = logging.FileHandler(logPath, mode="w")
    fileHandler.setFormatter(formatter)

    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    logging.debug("Logging configured to: %s", logPath)
    return logPath


def cleanLogsDir(logDir):
    if not os.path.exists(logDir):
        return
    for name in os.listdir(logDir):
        path = os.path.join(logDir, name)
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path, ignore_errors=True)
        except OSError as err:
            logging.warning("Failed to delete %s: %s", path, err)
