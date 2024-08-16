import unittest

# Import test cases
from android.test_android_feature1 import TestAndroidFeature1
from windows.test_windows_feature1 import TestWindowsFeature1

def suite():
    suite = unittest.TestSuite()
    # Add Android tests
    suite.addTest(TestAndroidFeature1('TestAndroidFeature1'))
    # Add Windows tests
    suite.addTest(TestWindowsFeature1('TestWindowsFeature1'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
