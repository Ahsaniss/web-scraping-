from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver with the correct service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Amazon's laptop category page
driver.get("https://www.amazon.com/s?k=laptop")

# Open a file to write the laptop names
with open("laptop_names.txt", "w", encoding="utf-8") as file:
    # Loop through multiple pages (pagination)
    while True:
        # Find all laptop titles
        laptop_names = driver.find_elements(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')

        # Find all laptop prices
        laptop_prices = []
        for laptop in laptop_names:
            try:
                price_whole = laptop.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
                price_fraction = laptop.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
                price = price_whole + "." + price_fraction  # Combine both parts
            except:
                price = 'N/A' # if price is missing
            laptop_prices.append(price)

        # Find all laptop ratings
        laptop_ratings = driver.find_elements(By.XPATH, '//span[@class="a-icon-alt"]')
        # save data to file
        for name, price, rating in zip(laptop_names, laptop_prices, laptop_ratings):
            file.write(f'Laptop Name: {name.text}, Laptop Prices: {price}, Laptop Ratings: {rating.text}\n')
            print(f'Laptop Name: {name.text}, Laptop Prices: {price}, Laptop Ratings: {rating.text}\n')

        # Check if there's a "Next" button to navigate to the next page
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 's-pagination-next')]")
            next_button.click()  # Click the "Next" button
            time.sleep(3)  # Wait for the next page to load
        except Exception as e:
            print("No more pages.")
            break  # Exit the loop if there's no "Next" button
driver.quit()