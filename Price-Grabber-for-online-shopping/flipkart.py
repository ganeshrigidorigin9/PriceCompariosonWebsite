from selenium import webdriver
from selenium.webdriver.common.by import By
flipkart_list = []
def flipkart_details(product_name):
    driver = webdriver.Chrome()
    url = f'https://www.flipkart.com/search?q={product_name}'
    driver.get(url)
    driver.implicitly_wait(10)
    product_elements = driver.find_elements(By.CLASS_NAME, '_2kHMtA')
    for item in product_elements[:3]:
        try:
            name = item.find_element(By.CLASS_NAME, '_4rR01T').text
            price = item.find_element(By.CLASS_NAME, '_30jeq3').text
        except Exception as e:
            print(f"Error parsing product details: {e}")

        try:
            image_link = item.find_element(By.CLASS_NAME, '_396cs4').get_attribute('src')
        except Exception as e:
            print(f"Error parsing image link: {e}")
            image_link = "N/A"
        try:
            product_link = item.find_element(By.CLASS_NAME, '_1fQZEK').get_attribute('href')
        except Exception as e:
            print(f"Error parsing image link: {e}")
            image_link = "N/A"

        try:
            rating = item.find_element(By.CLASS_NAME, '_3LWZlK').text
        except Exception as e:
            print(f"Error parsing product rating: {e}")
            rating = "N/A"
        flipkart_list.append([image_link,name,price,rating,product_link])
    driver.quit()
    return flipkart_list