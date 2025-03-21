import os
import sys
import logging

from sikuli import ImagePath, getBundlePath


class BaseTest:
    @classmethod
    def setupEnv(cls):
        bundleDir = os.path.dirname(getBundlePath())
        projectRoot = os.path.abspath(os.path.join(bundleDir, "."))
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
