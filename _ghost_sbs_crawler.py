from selenium import webdriver
import urllib.request


options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/noopy/ghoststation_transcript/downloadedmp3",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
  "headless": False
})
driver = webdriver.Chrome(r"/Applications/chromedriver", chrome_options=options)

url ="https://programs.sbs.co.kr/radio/sghost/gorealrapod/56929"
driver.get(url)

# element = driver.find_element_by_class_name('podcast_btn_download')
# print(element)

div = driver.find_element_by_class_name('podcast_btn_w')
print(div)
radio_mp3_link = div.find_element_by_css_selector('a').get_attribute('href')
# video_url = driver.get(radio_mp3_link)
urllib.request.urlretrieve(radio_mp3_link)


# driver.find_elements_by_partial_link_text("podcastdown").click()


"""
<a href="/radio/sghost/episodedownload?fileUrl=http%3A%2F%2Fpodcastdown.sbs.co.kr%2Fpowerfm%2F2018%2F12%2Fpodcast-v2000010307-20181228-549.mp3%3Fvod_id%3DV2000010307%26podcast_id%3DP0000000579" class="podcast_btn_download" title="다운로드" download="549회 담배 확실하게 끊는 방법, 007에 대해서, 미국보다 북한이 더 나빠">
                                <div class="podcast_btn_inner">
                                    <span class="prog_icn icon_download"><i class="ir">다운로드아이콘</i></span>
                                    <span class="btn_text">다운로드</span>
                                </div>
                            </a>
"""