import logging

from BaseTest import BaseTest


class TestEnvironmentHelper:
    def __init__(self, testClassName: str, baseTest: BaseTest):
        self.testClassName = testClassName
        self.base = baseTest

    def setupClassEnv(self):
        self.base.setupEnv()
        logging.info("Environment initialized for '%s'.", self.testClassName)

    def setupTestEnv(self):
        self.base.setupTestObjects()

    def teardownClassEnv(self):
        self.base.teardownEnv()
        logging.info("Environment cleaned for '%s'.", self.testClassName)

    def setupAll(self, test):
        test.screens = self.base.screens
        test.flow = self.base.flow

    @property
    def screens(self):
        return self.base.screens

    @property
    def flow(self):
        return self.base.flow

    @classmethod
    def setUpTestClass(cls, testClass):
        base = BaseTest()
        testClass.env = TestEnvironmentHelper(testClass.__name__, base)
        testClass.env.setupClassEnv()

    @staticmethod
    def setUpTestMethod(test):
        test.env.setupAll(test)
        test.env.setupTestEnv()
