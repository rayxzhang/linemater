from seleniumbase import BaseCase
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LinemateCrawler(BaseCase):
    def test_linemate_crawler(self):
        # Navigate to linemate.com
        self.open("https://linemate.io")
        
        # Wait for page to load
        self.wait_for_element("body", timeout=10)
      
        self.login()
        
        # Click the Home link in the navigation bar
        home_selector = "div.navigation-bar-middle a[href='/nfl']"
        self.wait_for_element(home_selector, timeout=10)
        self.click(home_selector)
    
        # Click the NFL dropdown
        dropdown_selector = "button.input-selection-trigger"
        self.wait_for_element(dropdown_selector, timeout=10)
        self.click(dropdown_selector)
    
        self.wait(10)

    def login(self):
        """Handle login if required"""
        from secret import username, password
        
        if not username or not password:
            raise ValueError("Missing login credentials in environment variables")
        
        # Click the login button in the navigation bar
        login_button = "div.navigation-bar-right-login-button-wrapper .button-container"
        self.click(login_button)
        
        # Fill in email and password fields
        self.type("div.login-page-form input[type='email']", username)
        self.type("div.login-page-form input[type='password']", password)
        
        # Click the login button
        self.click("div.login-page-form .button-container")
        
        # Wait for login to complete - using the avatar element as indicator
        self.wait_for_element(".navigation-bar-right-avatar-wrapper", timeout=10)

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])