import requests
import os

from tqdm import tqdm

import torchtext

WAR_AND_PEACE = "https://raw.githubusercontent.com/mmcky/nyu-econ-370/master/notebooks/data/book-war-and-peace.txt"
APPS = "https://people.eecs.berkeley.edu/~hendrycks/APPS.tar.gz"

def download_from_url(url, filename):
    if os.path.exists(filename):
        print(filename, "already found")
        return
    
    r = requests.get(url)
    with open(filename, "wb") as f: 
        for data in tqdm(r.iter_content(), desc="Downloading: {}".format(filename)):
            f.write(data)

def download_IWSLT2016(target_dir='./IWSLT2016'):
    if os.path.exists(target_dir):
        print(target_dir, "already exists")
        return 
        
    torchtext.datasets.IWSLT2016(root=target_dir)
    print("Downloaded IWSLT2016")

def download_wiki_corpora(language_code, dump):
    dump_name="{}wiki-{}-pages-articles-multistream.xml.bz2".format(language_code, dump)
    link="https://dumps.wikimedia.org/{}wiki/{}/".format(language_code, dump) + dump_name
    # download_from_url(link)

    # note: after downloading from wiki dumps
    # we are going to want to use wikiextractor
    # here: https://github.com/attardi/wikiextractor

if __name__ == "__main__":
    # download_wiki_corpora("fr", "20210120")
    download_from_url(WAR_AND_PEACE, "war_and_peace.txt")
    download_from_url(APPS, "war_and_peace.txt")
