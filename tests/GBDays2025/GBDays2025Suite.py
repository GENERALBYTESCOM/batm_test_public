import importlib
import logging
import os
import sys
import unittest

try:
    from sikuli import getBundlePath

    runnerDir = getBundlePath()
except ImportError:
    runnerDir = os.path.dirname(os.path.abspath(__file__))

testsDir = os.path.abspath(os.path.join(runnerDir, ".."))
if testsDir not in sys.path:
    sys.path.insert(0, testsDir)

testCases = [
    ("TestBTC", "testAnonymousBuyBTC"),
    ("TestLTC", "testAnonymousBuyLTC"),
    ("TestETH", "testAnonymousBuyETH"),
    ("TestLBTC", "testAnonymousBuyLBTC"),
]


def suite():
    testSuite = unittest.TestSuite()
    for moduleName, testName in testCases:
        testClass = getattr(importlib.import_module(moduleName), moduleName)
        testSuite.addTest(testClass(testName))
    return testSuite


def main():
    logging.basicConfig(level=logging.INFO)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    if not result.wasSuccessful():
        logging.error("GBDays2025 tests failed.")
    else:
        logging.info("All GBDays2025 tests passed successfully.")


if __name__ == "__main__":
    main()
