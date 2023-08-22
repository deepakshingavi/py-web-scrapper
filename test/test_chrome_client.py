import unittest

from browser.chrome_client import get_chrome_driver




def test_get_chrome_driver():
    driver = get_chrome_driver()
    assert driver
