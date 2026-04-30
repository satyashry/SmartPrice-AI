from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import sys
from src.exception import CustomException
from src.logger import logging
from pathlib import Path


chrome_options = Options()

def init_driver():
    logging.info("Program Started....")
    return webdriver.Chrome(options=chrome_options)

#getting the pand converting to html 
def get_page(driver, url):
    driver.get(url)
    time.sleep(3)
    return BeautifulSoup(driver.page_source, "html.parser")

# Scraping all pages
def scrape_all_pages(driver, total_pages):
    brands, original_prices, current_prices = [], [], []

    for page in range(1, total_pages + 1):
        url = f"https://www.flipkart.com/search?q=laptops&page={page}"
        soup = get_page(driver, url)

        for item in soup.find_all("div", class_="RG5Slk"):
            brands.append(item.get_text(strip=True))

        for item in soup.find_all("div", class_="kRYCnD gxR4EY"):
            original_prices.append(item.get_text(strip=True))

        for item in soup.find_all("div", class_="hZ3P6w DeU9vF"):
            current_prices.append(item.get_text(strip=True))
   
        print(f"Scraped page {page} ✅")
    logging.info("Scraping The Pages")
    
    return brands, original_prices, current_prices
    

# saving the data
def save_data(brands, original, current):
    max_len = max(len(brands), len(original), len(current))

    brands += [None] * (max_len - len(brands))
    original += [None] * (max_len - len(original))
    current += [None] * (max_len - len(current))

    df = pd.DataFrame({
        "brand": brands,
        "original_price": original,
        "current_price": current
    })

    folder_path = Path('notebook/data')
    folder_path.mkdir(parents=True, exist_ok=True)

    file_path = folder_path/'laptops_raw.csv'

    df.to_csv(file_path, index=False)
    print("Saved ✅", len(df))

    logging.info("Completed the Scraping and Saved the Data to DATAFRAME")
    logging.info("Program Ended!")




if __name__ == "__main__":
    driver = None

    try:
        driver = init_driver()
        print("Browser opened ✅")

        brands, original, current = scrape_all_pages(driver, 40)
        print("Scraping done ✅")

        save_data(brands, original, current)

    except Exception as e:
        raise CustomException(e, sys)

    finally:
        if driver:
            driver.quit()