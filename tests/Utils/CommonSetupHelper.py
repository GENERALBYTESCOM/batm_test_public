from Utils.TestEnvironmentHelper import TestEnvironmentHelper


class CommonTestBehavior:
    def __init__(self):
        pass

    def doCommonSetup(self, test):
        test.env = TestEnvironmentHelper(test.__class__.__name__)
        test.env.setupAll(test)
        test.env.setupTestEnv()

    def doCommonTeardown(self, test):
        if test.env:
            test.env.teardownClassEnv()
