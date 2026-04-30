from bs4 import BeautifulSoup
import selenium
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import time
import requests
from selenium.webdriver.chrome.options import Options



def get_page(url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)# keeps the browser Active
    driver = webdriver.Chrome(options = chrome_options)# opens a empty Chrome Browser connecting with the URL
    driver.get(url)
    time.sleep(2) # Allowing time for to load
    html = driver.page_source # changes the format to HTML

    return BeautifulSoup(html, "html.parser")

soup = get_page("https://www.flipkart.com/search?q=laptops&page=1")

def scrape_page(soup):

    brand = []
    actual_price = []
    current_price = []


    # for brand
    for i in soup.find_all("div", class_ = "RG5Slk"):
        brand.append(i.text)
    # for actual prices
    for i in soup.find_all("div", class_ = "kRYCnD gxR4EY") :
        actual_price.append(i.text)
    # for discount prices
    for i in soup.find_all("div", class_ = "hZ3P6w DeU9vF"):
        current_price.append(i.text)

    return brand,actual_price,current_price

# Scraping all pages
def  scrape_all_pages(total_pages):
    all_brands = []
    all_actual = []
    all_current = []

    for page in range(1,total_pages+1):
        url = f"https://www.flipkart.com/search?q=laptops&page={page}"
        soup_all = get_page(url)

        brand,actual,current = scrape_page(soup_all)
        
        all_brands.extend(brand)
        all_actual.extend(actual)
        all_current.extend(current)

        print(f"Scraped Page {page} ✅")

    return all_brands,all_actual,all_current
        
