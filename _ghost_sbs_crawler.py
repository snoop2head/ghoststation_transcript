from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, parse_qs
from multiprocessing.dummy import Pool as ThreadPool
import urllib3


# chrome driver options
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/noopy/ghoststation_transcript/downloadedmp3",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
})
options.add_argument('headless')
driver = webdriver.Chrome(r"/Applications/chromedriver", chrome_options=options)


# get target url 
url ="https://programs.sbs.co.kr/radio/sghost/gorealrapod/56929"
driver.get(url)

# parse webpage 
div = driver.find_element_by_class_name('podcast_btn_w')
print(div)
radio_mp3_link = div.find_element_by_css_selector('a').get_attribute('href')
print(radio_mp3_link)

# get mp3 file name
radio_link_queries_parsed = radio_mp3_link.split('/')
last_item_of_the_list = radio_link_queries_parsed[-1]
video_item_quries_parsed = last_item_of_the_list.split('%')
file_name = video_item_quries_parsed[7][11:]
print(file_name)


# download video with url open
resp = urllib.request.urlopen(radio_mp3_link)
respHTML = resp.read()
binfile = open("/Users/noopy/ghoststation_transcript/downloadedmp3/" + file_name, "wb")
binfile.write(respHTML)
binfile.close()

# download video with url retrieve with multithreading
# urllib.request.urlretrieve(radio_mp3_link)

# download video with FancyURL opener and retrieve
#test=urllib.request.urlopen() is not working, since it is for python 2.7
# test=urllib.request.FancyURLopener()
# test.retrieve(radio_mp3_link,file_name)



"""
<a href="/radio/sghost/episodedownload?fileUrl=http%3A%2F%2Fpodcastdown.sbs.co.kr%2Fpowerfm%2F2018%2F12%2Fpodcast-v2000010307-20181228-549.mp3%3Fvod_id%3DV2000010307%26podcast_id%3DP0000000579" class="podcast_btn_download" title="다운로드" download="549회 담배 확실하게 끊는 방법, 007에 대해서, 미국보다 북한이 더 나빠">
                                <div class="podcast_btn_inner">
                                    <span class="prog_icn icon_download"><i class="ir">다운로드아이콘</i></span>
                                    <span class="btn_text">다운로드</span>
                                </div>
                            </a>
"""