"""
    Selenium Cookie Issue
    Copyright (C) 2023 Emil Hemdal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pytest
import time

from selenium import webdriver

class TestVccPage:
    def test_run_chrome(self, chrome_browser: webdriver.Chrome):
        chrome_browser.get('https://www.volvocars.com/intl/v/safety/highlights')

        chrome_browser.refresh()
        
        time.sleep(3)

        assert True

    def test_run_firefox(self, firefox_browser: webdriver.Firefox):
        firefox_browser.get('https://www.volvocars.com/intl/v/safety/highlights')

        firefox_browser.refresh()

        time.sleep(3)

        assert True

@pytest.fixture
def chrome_browser():
    browser = webdriver.Chrome()
    browser.delete_all_cookies() # clean slate
    yield browser
    browser.quit()

@pytest.fixture
def firefox_browser():
    browser = webdriver.Firefox()
    browser.delete_all_cookies() # clean slate
    yield browser
    browser.quit()
