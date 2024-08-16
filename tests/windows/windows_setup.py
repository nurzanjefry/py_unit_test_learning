import unittest
from pywinauto import Application
import yaml
import time


class WindowsSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Common setup for Windows tests."""
        with open('config/config.yaml', 'r') as file:
            cls.config = yaml.safe_load(file)
        cls.app_path = cls.config['windows_app_path']
        cls.app = None
        cls.window = None

    @classmethod
    def start_application(cls):
        """Start the Windows application."""
        cls.app = Application().start(cls.app_path)
        time.sleep(5)  # Wait for the app to load
        cls.window = cls.app.window(title_re=".*Application Title.*")
        cls.window.wait('visible', timeout=10)

    @classmethod
    def tearDownClass(cls):
        """Common teardown for Windows tests."""
        if cls.app:
            cls.app.kill()
