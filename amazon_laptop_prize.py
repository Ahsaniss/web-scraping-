from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Amazon Laptop Search Page
url = "https://www.amazon.com/s?k=laptop"
driver.get(url)
time.sleep(5)  # Allow time for page to load

# Extract laptop details
laptop_cards = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for laptop in laptop_cards:
    try:
        category = laptop.find_element(By.XPATH, './/h2').text
    except:
        category = "Unknown"

    try:
        rating_element = laptop.find_element(By.XPATH, './/span[@class="a-icon-alt"]')
        rating = rating_element.get_attribute('aria-label')
    except:
        rating = None

    try:
        price_whole = laptop.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
        price_fraction = laptop.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
        price = f"${price_whole}.{price_fraction}"
    except:
        price = "N/A"

    print(f"Category: {category}")
    if rating:
        print(f"Rating: {rating}")
    print(f"Price: {price}")
    print("-" * 50)

# Close the browser
driver.quit()
