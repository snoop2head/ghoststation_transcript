from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs
import time


# chrome driver options
options = webdriver.ChromeOptions()
options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": r"/Users/noopy/ghoststation_transcript/downloadedmp3",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)
# options.add_argument("headless")
driver = webdriver.Chrome(r"/Applications/chromedriver", chrome_options=options)


# get target url
url = "https://programs.sbs.co.kr/radio/sghost/gorealrapod/56929"
driver.get(url)


page_count = 1
while True:
    # Increase page_count value on each iteration on +1
    page_count += 1
    # Do what you need to do on each page
    # Code goes here
    try:
        # Clicking on "2" on pagination on first iteration, "3" on second...
        page_number = str(page_count)

        # clicking to paginate
        driver.find_element_by_id(
            f"program-front-radio-pagination-page-{page_number}"
        ).click()

        # waiting for page to load in order to prevent staele element error
        time.sleep(3)

    except NoSuchElementException:
        # Stop loop if no more page available
        break
