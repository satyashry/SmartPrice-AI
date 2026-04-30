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

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)# keeps the browser Active
driver = webdriver.Chrome(options = chrome_options)# opens a empty Chrome Browser connecting with the URL

def get_page(url):
    driver.get(url)
    time.sleep(2) # Allowing time for to load
    html = driver.page_source # changes the format to HTML
    return BeautifulSoup(html, "html.parser")

soup = get_page("https://www.flipkart.com/search?q=laptops&page=1")


# Scraping all pages
def  scrape_all_pages(total_pages):
    all_brands ,all_actual,all_current = [],[],[]

    for page in range(1, total_pages + 1):
        url = f"https://www.flipkart.com/search?q=laptops&page={page}"

        soup_all = get_page( url)

        
    # for brand
        for i in soup_all.find_all("div", class_ = "RG5Slk"):
            all_brands.append(i.text)
    # for actual prices
        for i in soup_all.find_all("div", class_ = "kRYCnD gxR4EY") :
            all_actual.append(i.text)
    # for discount prices
        for i in soup_all.find_all("div", class_ = "hZ3P6w DeU9vF"):
            all_current.append(i.text)

        print(f"Scraped Page {page} ✅")

    return all_brands,all_actual,all_current
        
brands, original_price, current_price = scrape_all_pages(92)



# save to CSV
max_len = max(len(brands), len(original_price), len(current_price))

while len(brands) < max_len:
    brands.append(None)
while len(original_price) < max_len:
    original_price.append(None)
while len(current_price) < max_len:
    current_price.append(None)

df = pd.DataFrame({
    "brand": brands,
    "original_price": original_price,
    "current_price": current_price
})

df.to_csv("laptops_raw.csv", index=False)
print("Saved!", len(df))