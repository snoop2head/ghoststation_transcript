from BeautifulSoup import BeautifulSoup
from functools import partial
from urllib3 import urlretrieve
from urlparse import urljoin, urlparse
import argparse
import multiprocessing
import os
import sys
import urllib3

def get_url():
    parser = argparse.ArgumentParser(description='Download images from a website')
    parser.add_argument('-w', type=str, help='website url')
    options = parser.parse_args()
    if options.w is None:
        print(parser.print_help())
        sys.exit()
    return options.w

def save_image(image, site_url, folder):
    filename = image['src'].split('/')[-1]
    outpath = os.path.join(folder, filename)
    url = urljoin(site_url, image['src'])
    urlretrieve(url, outpath)
    print('Saved image ' + outpath)

if __name__ == '__main__':
    url = get_url()
    os.mkdir(urlparse(url).netloc)
    page = BeautifulSoup(urllib3.urlopen(url).read())
    images = page.findAll('img')
    pool = multiprocessing.Pool()
    partial_save_image = partial(save_image, site_url=url, folder=urlparse(url).netloc)
    pool.map(partial_save_image, images)
