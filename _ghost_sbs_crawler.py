from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs
import time
import glob


# designate target url
url = "https://programs.sbs.co.kr/radio/sghost/gorealrapod/56929"

# chrome driver options: downloading option and headless
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
options.add_argument("headless")

driver = webdriver.Chrome(r"/Applications/chromedriver", chrome_options=options)

# open url link with driver
driver.get(url)

# get file list that already exist in ./downloadedmp3
mp3_file_list = glob.glob("downloadedmp3/*.mp3")
print(mp3_file_list)

# first page
page_count = 1
while True:
    # parse webpage
    divs = driver.find_elements_by_class_name("podcast_btn_w")
    # print(divs)
    for div in divs:
        radio_mp3_link = div.find_element_by_css_selector("a").get_attribute("href")
        # print(radio_mp3_link)

        # get mp3 file name
        radio_link_queries_parsed = radio_mp3_link.split("/")
        last_item_of_the_list = radio_link_queries_parsed[-1]
        video_item_quries_parsed = last_item_of_the_list.split("%")
        file_name = video_item_quries_parsed[7][11:]

        # if mp3 file exists in folder, don't download.
        if any(file_name in s for s in mp3_file_list):
            print(file_name + " already exists")
            pass
        # if mp3 file does not exist in folder, then download
        else:
            # download video with url open
            resp = urllib.request.urlopen(radio_mp3_link)
            respHTML = resp.read()
            binfile = open(
                "/Users/noopy/ghoststation_transcript/downloadedmp3/" + file_name, "wb"
            )
            binfile.write(respHTML)
            binfile.close()
            print(file_name + " is downloaded")

    # get next bundle of 10 pages
    # print(page_count)
    if page_count % 10 == 0:
        driver.find_element_by_id("program-front-radio-pagination-next").click()
        time.sleep(3)
    else:
        pass

    # Increase page_count value on each iteration on +1
    page_count += 1

    # paginate
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


"""
# tag structure
<a href="/radio/sghost/episodedownload?fileUrl=http%3A%2F%2Fpodcastdown.sbs.co.kr%2Fpowerfm%2F2018%2F12%2Fpodcast-v2000010307-20181228-549.mp3%3Fvod_id%3DV2000010307%26podcast_id%3DP0000000579" class="podcast_btn_download" title="다운로드" download="549회 담배 확실하게 끊는 방법, 007에 대해서, 미국보다 북한이 더 나빠">
                                <div class="podcast_btn_inner">
                                    <span class="prog_icn icon_download"><i class="ir">다운로드아이콘</i></span>
                                    <span class="btn_text">다운로드</span>
                                </div>
                            </a>
"""

# download video with url retrieve -> Too Slow
# urllib.request.urlretrieve(radio_mp3_link)

# download video with FancyURL opener and retrieve -> Not working
# test=urllib.request.urlopen() is not working, since it is for python 2.7
# test=urllib.request.FancyURLopener()
# test.retrieve(radio_mp3_link,file_name)
