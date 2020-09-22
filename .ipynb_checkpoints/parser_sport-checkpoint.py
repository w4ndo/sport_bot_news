from selenium import webdriver
from time import sleep
import pandas as pd
from typing import List
import os


def init(url: str = 'https://www.championat.com/'):
    # Init options:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    # Start web_driver:
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
#     driver.maximize_window()
    return driver

def base_auth(driver) -> None:
    button = driver.find_elements_by_class_name('button._primary.show-more.js-show-more')[1]
    button.click()


def parse_news(url: str, driver) -> List[str]:
    driver.get(url)
    sleep(1)
    head = driver.find_element_by_class_name('article-head__title').text
    time = driver.find_element_by_class_name('article-head__date').text
    tags = driver.find_element_by_class_name('article-head__tag').text
    return [head, time, tags, url]

def parse(driver) -> pd.DataFrame:
    main_news = driver.find_elements_by_class_name('news-items')[1]
    result = []
    urls = []
    for i in main_news.find_elements_by_class_name('news-item__title'):
        url = i.get_attribute('href')
        urls.append(url)

    for url in urls:
        res = parse_news(url, driver)
        result.append(res)

    df = pd.DataFrame(result, columns=['head', 'time', 'tags', 'url'])
    return df
    

def main():
    driver = init()
    base_auth(driver)
    df = parse(driver)
    driver.close()
    return df


if __name__ == '__main__':
    main()