from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazon_list = []
flipkart_list = []

def amazon_details(product_name):
    amazon_list = []
    driver = webdriver.Chrome()
    url = f'https://www.amazon.in/s?k={product_name}'
    driver.get(url)
    driver.implicitly_wait(10)
    try:
        # Wait for product elements to be present in the DOM
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 's-asin')))
        
        product_elements = driver.find_elements(By.CLASS_NAME, 's-asin')
        for item in product_elements[:3]:  # Get details of the first 3 products
            product_info = []
            try:
                name = item.find_element(By.CLASS_NAME, 'a-text-normal').text
                price = item.find_element(By.CLASS_NAME, 'a-price-whole').text
                image_link = item.find_element(By.CLASS_NAME, 's-image').get_attribute('src')
                product_link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')
                rating_element = item.find_element(By.CSS_SELECTOR, '.a-popover-trigger .a-icon-alt')
                rating = rating_element.get_attribute('textContent')
                product_info = [image_link,name,price,rating,product_link]
            except Exception as e:
                print(f"Error parsing product details: {e}")
            if product_info:
                amazon_list.append(product_info)
    except Exception as e:
        print(f"Error: {e}")

    driver.quit()
    return amazon_list