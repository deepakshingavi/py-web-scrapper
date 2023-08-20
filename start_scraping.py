from browser.chrome_client import get_chrome_driver
import sys

from scrapper.docker_hub_scrapper import DockerHubScraper
import datetime

from writer.csv_writer import CsvWriter

driver = None
scraper = None
web_data_arr = []
if len(sys.argv) < 4:
    raise Exception(
        f"Insufficient parameters. Please re-execute script as `start_scraping.py <browser> <website> <writer>`.")
try:
    if sys.argv[1] == 'chrome':
        driver = get_chrome_driver()
    else:
        raise Exception(f"{sys.argv[1]} browser not supported")

    if sys.argv[2] == 'hub.docker.com':
        scraper = DockerHubScraper(driver)
    else:
        raise Exception(f"Web Scraper for site '{sys.argv[2]}' is not implemented yet.")

    if scraper:
        web_data_arr = scraper.get_data()

except Exception as e:
    print(f"Error occurred while scraping browser={sys.argv[1]} for website={sys.argv[2]} error={e}")
    raise e
finally:
    if driver:
        driver.quit()

if sys.argv[3] == 'csv':
    csv_file_name = f'results_{datetime.datetime.now().strftime("%d_%b_%Y_%H_%M_%S")}.csv'
    writer = CsvWriter(csv_file_name)
else:
    raise Exception(f"Implementation for writing to '{sys.argv[3]}' is not implemented yet.")

writer.write(web_data_arr)
