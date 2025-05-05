import logging
import os
import shutil
import sys
import unittest

from sikuli import getBundlePath


def cleanFailedScreenshots():
    runnerDir = getBundlePath()
    screenshotsDir = os.path.abspath(
        os.path.join(runnerDir, "..", "tests", "FailedScreenshots")
    )
    if os.path.exists(screenshotsDir):
        shutil.rmtree(screenshotsDir)
    os.makedirs(screenshotsDir)
    logging.info("Failed screenshots directory prepared: %s", screenshotsDir)


def main():
    runnerDir = getBundlePath()
    testsDir = os.path.abspath(os.path.join(runnerDir, "..", "tests"))
    if testsDir not in sys.path:
        sys.path.insert(0, testsDir)

    cleanFailedScreenshots()
    suite = unittest.defaultTestLoader.discover(testsDir, pattern="Test*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()
