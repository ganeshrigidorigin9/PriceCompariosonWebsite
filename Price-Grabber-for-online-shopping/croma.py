import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
""" import lxml """
from googlesearch import search
from bs4 import BeautifulSoup
croma_list=[]
def croma_details(product_name):
    wait_imp = 10
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--start-maximized')

    # Create a WebDriver instance
    wd = webdriver.Chrome(options=chrome_options)
    urls = []
    product_link=''
    query = "{} Croma".format(product_name)
    for i in search(query, tld="co.in", num=3, stop=3, pause=7):
        urls.append(i)
        """ print(i) """

    for i in range(len(urls)):
        wd.get(urls[i])
        wd.implicitly_wait(wait_imp)
        product_link=urls[i]
        product_name = ''
        product_price = ''
        product_rating = ''
        product_image = ''
        try:
            product_price_element = wd.find_element(By.CLASS_NAME, "amount")
            product_price = product_price_element.text
        except:
            product_price = "Currently Unavailable"
        try:
            product_title_element = wd.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/h1")
            product_name = product_title_element.text
        except:
            product_name = "NA"
        try:
            product_rating_element = wd.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/div[1]/span[1]/span")
            product_rating = product_rating_element.text
        except:
            product_rating = "NA"
        try:
            product_image_element = wd.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/span/img")
            product_image = product_image_element.get_attribute('src')
        except:
            product_image = "NA"
        croma_list.append([product_image,product_name,product_price,product_rating,product_link])
    return croma_list
