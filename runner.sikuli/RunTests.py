import os
import sys
import unittest

from sikuli import getBundlePath


def main():
    runnerDir = getBundlePath()
    testsDir = os.path.abspath(os.path.join(runnerDir, "..", "tests"))
    if testsDir not in sys.path:
        sys.path.append(testsDir)

    suite = unittest.defaultTestLoader.discover(testsDir, pattern="Test*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()
