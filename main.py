import unittest
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
import time
import HtmlTestRunner  # Import the HTMLTestRunner

class SteamAutomationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup before any tests are run."""
        cls.app_path = r"C:\Program Files (x86)\Steam\Steam.exe"  # Adjust path as needed
        cls.app = None
        cls.steam_window = None

    def test_1_launch_steam(self):
        """Test case: Launch Steam application."""
        try:
            self.app = Application().start(self.app_path)
            time.sleep(5)  # Wait for the app to load
            self.assertIsNotNone(self.app, "Steam did not start.")
        except Exception as e:
            self.fail(f"Failed to start Steam: {e}")

    def test_2_check_steam_open(self):
        """Test case: Check if Steam is open and running."""
        self.assertIsNotNone(self.app, "Steam application was not started in previous test.")
        try:
            self.steam_window = self.app.window(title_re=".*Steam.*")
            self.steam_window.wait('visible', timeout=10)
            self.assertIsNotNone(self.steam_window, "Steam window is not visible.")
        except ElementNotFoundError:
            self.fail("Steam window not found.")

    def test_3_interact_with_whats_new(self):
        """Test case: Interact with 'What's New' section."""
        self.assertIsNotNone(self.steam_window, "Steam window was not detected in previous test.")
        try:
            self.steam_window.set_focus()
            whats_new_button = self.steam_window.child_window(title="What's New", control_type="Button")
            if whats_new_button.exists():
                whats_new_button.click()
                self.assertTrue(True, "Clicked on 'What's New'.")
            else:
                self.fail("'What's New' section not found.")
        except ElementNotFoundError:
            self.fail("Could not find the 'What's New' section.")

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests are done."""
        if cls.app is not None:
            try:
                cls.app.kill()
            except Exception as e:
                print(f"Failed to close Steam: {e}")

if __name__ == "__main__":
    # Use HTMLTestRunner to run tests and generate an HTML report
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='steam_automation_reports', report_name="SteamAutomationReport")
    )
