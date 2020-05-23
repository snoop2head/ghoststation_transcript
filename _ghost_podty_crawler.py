from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs
import time


# designate target url
url = "https://www.podty.me/cast/171606"
query = "/episodes?page="
page_number = 1

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

# open url link with driver
driver.get(url)


page_count = 1
while True:
    # parse webpage
    divs = driver.find_elements_by_class_name("podcast_btn_w")
    # print(divs)
    for div in divs:
        radio_mp3_link = div.find_element_by_css_selector("a").get_attribute("href")
        print(radio_mp3_link)

        # get mp3 file name
        radio_link_queries_parsed = radio_mp3_link.split("/")
        last_item_of_the_list = radio_link_queries_parsed[-1]
        video_item_quries_parsed = last_item_of_the_list.split("%")
        file_name = video_item_quries_parsed[7][11:]
        print(file_name)
        # download video with url open
        resp = urllib.request.urlopen(radio_mp3_link)
        respHTML = resp.read()
        binfile = open(
            "/Users/noopy/ghoststation_transcript/downloadedmp3/" + file_name, "wb"
        )
        binfile.write(respHTML)
        binfile.close()

    # Increase page_count value on each iteration on +1
    page_count += 1

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

# download video with url retrieve with multithreading
# urllib.request.urlretrieve(radio_mp3_link)

# download video with FancyURL opener and retrieve
# test=urllib.request.urlopen() is not working, since it is for python 2.7
# test=urllib.request.FancyURLopener()
# test.retrieve(radio_mp3_link,file_name)


"""
# tag structure
<li data-cast-srl="171606" data-episode-srl="10974004" data-play-uri="https://cdn-cf.podty.me/meta/episode_audio/495/1545285056191.mp3" data-item-type="audio/mp3" data-episode-name="2002.12.30-마왕의 월차 재충전" data-liked="false" data-adult="false">
			<div class="episodeInfo">
				<p data-episode-name="2002.12.30-마왕의 월차 재충전">
                    <span class="tag_19 tag_small" name="episode19Tag" style="">19세이상 콘텐츠</span>
                    <a href="/episode/10974004">2002.12.30-마왕의 월차 재충전</a>
                </p>
				<time class="date">2018.12.21</time>
				<span class="count">재생/다운로드 3,204</span>
				<span class="comments" onclick="podty.pjax.go(g_urlSecureBase+'/episode/'+10974004+'?focus=c')"><a href="/episode/10974004?focus=c">댓글 22</a></span>
				<time class="playTime">
						0:09:49
				</time>
			</div>
			<div class="playTime"><time>
					0:09:49
			</time></div>
			<div class="btns play">
				<span><button class="btnPlayEpisode mp3" data-format="mp3">에피소드 mp3 재생</button></span>
			</div>
		</li>
"""
