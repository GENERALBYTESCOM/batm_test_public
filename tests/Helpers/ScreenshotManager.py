import logging
import os
import shutil
import sys

from Helpers.LoggingHelper import generateFileName
from sikuli import Screen


def ensureScreenshotsDir(screenshotsDir):
    if not os.path.exists(screenshotsDir):
        os.makedirs(screenshotsDir)
    for fileName in os.listdir(screenshotsDir):
        filePath = os.path.join(screenshotsDir, fileName)
        try:
            if os.path.isfile(filePath) or os.path.islink(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath)
        except OSError as e:
            logging.warning("Failed to delete file %s: %s", filePath, e)


def captureScreenshot(screenshotsDir, testName):
    if not isinstance(testName, str) or not testName.strip():
        logging.error("Invalid test name for screenshot")
        return None

    finalFileName = generateFileName(testName, "png", prefix="FAILED_")
    finalPath = os.path.join(screenshotsDir, finalFileName)
    try:
        screen = Screen()
        img = screen.capture()
        srcPath = str(img.getFile())

        if not os.path.exists(srcPath):
            raise RuntimeError("Captured image file not found at: {}".format(srcPath))

        dstPath = str(os.path.join(screenshotsDir, finalFileName))
        shutil.copy(srcPath, dstPath)
        logging.info("Screenshot saved: %s", finalPath)
        return finalPath

    except OSError as e:
        logging.error("Could not capture screenshot: %s", e)
        return None


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
