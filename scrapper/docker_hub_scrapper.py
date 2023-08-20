import time
import re

from bs4 import BeautifulSoup

from scrapper.base_scraper import BaseScraper


class DockerHubScraper(BaseScraper):

    def __init__(self, driver):
        self.driver = driver

    def get_data(self):
        image_info_list = []

        counter = 1
        while True:
            # Load the HTML page
            self.driver.get(
                "https://hub.docker.com/search?q=&type=image&image_filter=official&operating_system=linux"
                "&architecture"
                "=arm64&page=" + str(counter))
            time.sleep(2)

            # Wait to load the contents of the HTML FIle
            time.sleep(2)

            # Parse processed webpage with BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, features="html.parser")

            next_check = soup.find('p', attrs={'class': 'styles__limitedText___HDSWL'})

            if not isinstance(next_check, type(None)):
                break

            results = soup.find(id="searchResults")

            if isinstance(results, type(None)):
                print("Error: results is NoneType")
                break

            images_list = results.find_all('a', attrs={'data-testid': 'imageSearchResult'})

            if len(images_list) == 0:
                break  # Stopping the parsing when no images are found

            for image in images_list:

                # Getting the Name of the Image
                image_name = image.find('span', {"class": re.compile('.*MuiTypography-root.*')}).text

                attribute_values = image.find_all('p',
                                                  {"class": re.compile(
                                                      '.*MuiTypography-root MuiTypography-body1.*')})
                star_values = image.find_all('span',
                                             {"class": re.compile('.*MuiTypography-root MuiTypography-body1.*')})
                star_count = 0
                pull_count = 0
                # Download Counts
                if len(attribute_values) < 2:
                    download_count = attribute_values[0].text
                else:
                    download_count = attribute_values[0].text
                    pull_count = (attribute_values[1].text.replace("Pulls: ", "")
                                  .replace(",", ""))
                if len(star_values) > 1:
                    star_count = star_values[1].text

                # Writing the Image Name, Download Count and Stars Count to File
                image_info_list.append((image_name, download_count, star_count, pull_count))
                # writer.writerow([image_name, download_count, star_count, pull_count])

            if len(images_list) == 0:
                break

            counter += 1

        return image_info_list
        # Closing of the CSV File Handle

# Change the base_dir with your path.
# base_dir = '/Users/dshingav/Downloads' + os.sep

# Opening the CSV File Handle


# # Create the csv writer
# csv_file = open('results.csv', 'w')
# writer = csv.writer(csv_file)
#
# # Writing the Headers for the CSV File
# writer.writerow(['Image Name', 'Downloads', 'Stars', 'Pulls'])
#
# for image_info in image_info_arr:
#     writer.writerow(image_info)
#
# csv_file.close()
