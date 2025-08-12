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
        testName = detectTestName() or "test"

    if not os.path.exists(logDir):
        os.makedirs(logDir)

    logPath = os.path.join(
        logDir, "{}_{}.log".format(testName, datetime.now().strftime("%Y%m%d_%H%M%S"))
    )

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    oldHandlers = list(root.handlers)
    for h in oldHandlers:
        root.removeHandler(h)
        if isinstance(h, logging.FileHandler):
            try:
                h.close()
            except (OSError, ValueError):
                logging.debug("Ignoring error closing FileHandler %r", h, exc_info=True)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S"
    )

    fileHandler = logging.FileHandler(logPath, mode="w")
    fileHandler.setFormatter(formatter)
    root.addHandler(fileHandler)

    hasStream = any(
        isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
        for h in oldHandlers
    )
    if hasStream:
        for h in oldHandlers:
            if isinstance(h, logging.StreamHandler) and not isinstance(
                h, logging.FileHandler
            ):
                h.setFormatter(formatter)
                root.addHandler(h)
    else:
        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(formatter)
        root.addHandler(streamHandler)

    logging.info("Logging configured. File: %s", logPath)
    return logPath


def cleanLogsDir(logDir):
    if not os.path.exists(logDir):
        return
    for name in os.listdir(logDir):
        path = os.path.join(logDir, name)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
        except OSError as err:
            logging.warning("Failed to delete %s: %s", path, err)


def generateFileName(testName, fileType="log", prefix=""):
    return "{}{}_{}.{}".format(
        prefix, testName, datetime.now().strftime("%Y%m%d_%H%M%S"), fileType
    )
