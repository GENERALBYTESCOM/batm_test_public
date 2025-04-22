import logging
import os
import shutil
import time

from sikuli import Screen


def ensureScreenshotsDir(screenshotsDir):
    if os.path.exists(screenshotsDir):
        logging.debug("Cleaning screenshot directory: %s", screenshotsDir)
        shutil.rmtree(screenshotsDir)
    os.makedirs(screenshotsDir)
    logging.debug("Created screenshot directory: %s", screenshotsDir)


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
    testCase.baseTest.handleFailureScreenshot(testCase)
    logging.info("Test '%s' cleaned up successfully.", getTestMethodName(testCase))
