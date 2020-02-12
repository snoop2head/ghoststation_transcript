from selenium import webdriver
import urllib.request
from urllib.parse import urlparse, parse_qs
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing


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

# parse webpage and create list of urls
radio_link_list = []
divs = driver.find_elements_by_class_name('podcast_btn_w')
for div in divs:
    radio_mp3_link = div.find_element_by_css_selector('a').get_attribute('href')
    print(radio_mp3_link)
    radio_link_list.append(radio_mp3_link)
print(radio_link_list)

# get mp3 file name
def get_file_name_as_mp3(radio_mp3_link):
    radio_link_queries_parsed = radio_mp3_link.split('/')
    last_item_of_the_list = radio_link_queries_parsed[-1]
    video_item_quries_parsed = last_item_of_the_list.split('%')
    file_name = video_item_quries_parsed[7][11:]
    print(file_name)
    return file_name

# get file name list
file_name_list = []
for item in radio_link_list:
    file_name_list.append(get_file_name_as_mp3(item))
print(file_name_list)


import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

def print_head(url):
    print ('Starting %s' % url)
    data = urllib.request.FancyURLopener()
    radio_link_queries_parsed = radio_mp3_link.split('/')
    last_item_of_the_list = radio_link_queries_parsed[-1]
    video_item_quries_parsed = last_item_of_the_list.split('%')
    file_name = video_item_quries_parsed[7][11:]
    data.retrieve(radio_mp3_link,file_name)
    # print ('%s: %s bytes: %r' % (url, len(data), data[:50]))

jobs = [gevent.spawn(print_head, url) for url in radio_link_list]
gevent.joinall(jobs)

# from multiprocessing import Process
# from urllib.request import urlretrieve

# args = zip(radio_link_list, file_name_list)
# for arg in args:
#     p = Process(target = urlretrieve, args = arg)
#     p.start()

# results = Pool(4).starmap(urlretrieve, zip(urls, filenames))


# def download_mp3(link,file_name):
#   try:
#       urllib.request.urlretrieve(link, file_name+".mp3")
#   except:
#       pass

# urls = radio_link_list
# array_of_urls = 

# number_of_workers = 2
# with Pool(number_of_workers) as p:
#         print(p.map(download_mp3(url), ))


# filenames = radio_link_list
# results = Pool(10).starmap(download_mp3(link,get), zip(urls, filenames))


# def do_something(number, another_number):
#     return number ** 2 + another_number ** 2)

# array_of_number_tuple = [(x, x + 1) for x in range(0, 100000000000)]
# with Pool(number_of_workers) as p:
#     print(p.starmap(do_something, array_of_number_tuple))


# urls = radio_link_list
# pool = ThreadPool(100)
# results = pool.starmap(download_mp3, zip(links, d))

# with multiprocessing.Pool(processes=3) as pool:
#     results = pool.starmap(merge_names, product(names, repeat=2))
