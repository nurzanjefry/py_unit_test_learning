import unittest
from appium import webdriver
import yaml


class AndroidSetup(unittest.TestCase):
    desired_caps = None
    driver = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Common setup for Android tests."""
        with open('config/config.yaml', 'r') as file:
            cls.config = yaml.safe_load(file)
        cls.desired_caps = {
            'platformName': 'Android',
            'deviceName': cls.config['android_device_name'],
            'app': cls.config['android_app_path']
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)

    @classmethod
    def tearDownClass(cls):
        """Common teardown for Android tests."""
        if cls.driver:
            cls.driver.quit()
