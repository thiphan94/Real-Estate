import os
import time
import re

import random
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox import options as firefox_options
from selenium.webdriver.firefox.options import Options

def get_page(count=1):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    pages = []
    for page_nb in range(1, count + 1):
        # page_url = f"https://www.logic-immo.com/vente-immobilier/options/grouplocalities=13772_2,21249_2,5698_2,31111_2,19095_2,3482_2/groupprptypesids=2/page={page_nb}"
        page_url = f"https://www.seloger.com/list.htm?projects=2%2C5&types=2%2C1&natures=1%2C2%2C4&places=%5B%7B%22inseeCodes%22%3A%5B780311%5D%7D%5D&enterprise=0&qsVersion={page_nb}"
        driver.get(page_url)
        # Randomize waiting time
        time.sleep(random.uniform(5, 15))
        pages.append(driver.page_source.encode("utf-8"))

    driver.quit()
    return pages

def save_pages(pages):
    os.makedirs("data", exist_ok=True)
    for page_nb, page in enumerate(pages):
        with open(f"data/page_{page_nb}.html", "wb") as f_out:
            f_out.write(page)

def main():
    pages = get_page()
    save_pages(pages)

if __name__ == "__main__":
    main()