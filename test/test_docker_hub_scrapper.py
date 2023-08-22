import unittest
from unittest.mock import Mock

from browser.chrome_client import get_chrome_driver
from scrapper.docker_hub_scrapper import DockerHubScraper


class TestDockerHubScraper(unittest.TestCase):
    driver = Mock()
    def test_get_data(self):
        driver =  get_chrome_driver()
        scraper = DockerHubScraper(driver)
        self.assertTrue(scraper.get_data())
        driver.close()
