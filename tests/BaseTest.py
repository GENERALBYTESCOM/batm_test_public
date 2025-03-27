import logging
import os
import sys

from sikuli import ImagePath, getBundlePath


class BaseTest:
    def setupEnv(self):
        bundleDir = os.path.dirname(getBundlePath())
        projectRoot = os.path.abspath(bundleDir)
        if projectRoot not in sys.path:
            sys.path.append(projectRoot)

        pagesDir = os.path.join(projectRoot, "tests", "Screens")
        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        if pagesDir not in sys.path:
            sys.path.append(pagesDir)

        if screenshotsDir not in list(ImagePath.getPaths()):
            ImagePath.add(screenshotsDir)

        logging.basicConfig(
            format="[%(levelname)s] %(asctime)s - %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )
        logging.info("BaseTest.setupEnv: environment configured successfully.")

    def teardownEnv(self):
        logging.info("BaseTest.teardownEnv: environment cleanup completed.")
