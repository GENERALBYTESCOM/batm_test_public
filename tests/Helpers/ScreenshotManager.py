import logging
import os
import sys
import time

from sikuli import Screen


def ensureScreenshotsDir(screenshotsDir):
    if not os.path.exists(screenshotsDir):
        os.makedirs(screenshotsDir)
    for fileName in os.listdir(screenshotsDir):
        filePath = os.path.join(screenshotsDir, fileName)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
        except OSError as e:
            logging.warning("Failed to delete file %s: %s", filePath, e)


def captureScreenshot(screenshotsDir, testName):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    finalFileName = "FAILED_{}_{}.png".format(testName, timestamp)
    finalPath = os.path.join(screenshotsDir, finalFileName)
    try:
        screen = Screen()
        img = screen.capture()
        savedPath = img.getFile()
        os.rename(savedPath, finalPath)
        logging.info("Screenshot saved: %s", finalPath)
        return finalPath
    except (OSError, ValueError) as ex:
        logging.error("Failed to capture screenshot: %s", ex)
        return None
    finally:
        logging.debug("captureScreenshot attempted to save: %s", finalPath)
        logging.debug("file exists? %s", os.path.exists(finalPath))


def getTestClassAndMethod(testInstance):
    parts = testInstance.id().split(".")
    return "{}.{}".format(parts[-2], parts[-1])


def getTestMethodName(testInstance):
    return testInstance.id().split(".")[-1]


def safeSetUp(testCase, coin):
    try:
        testCase.screens.dashboardScreen.clickCoinButton(coin)
    except Exception:
        testCase.baseTest.handleFailureScreenshot(testCase)
        raise
    logging.info("Test '%s' setUp done.", getTestMethodName(testCase))


def safeTearDown(testCase):
    if sys.exc_info()[0] is not None:
        testCase.baseTest.handleFailureScreenshot(testCase)
    logging.info("Test '%s' cleaned up successfully.", getTestMethodName(testCase))
