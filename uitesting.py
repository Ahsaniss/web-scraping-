from scraper import webdriver
from scraper.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Edge()

# Correct File Path
file_path = "D:/CLASS%206TH%20SEME/New%20folder%20(3)/main.html"
driver.get(f"file:///{file_path}")

try:
    # Wait for the page to load
    time.sleep(2)

    # *1. Extract using Tag Name*
    title = driver.find_element(By.XPATH, "//h1").text
    print("Title:", title)

    # *2. Extract using XPath*
    paragraph = driver.find_element(By.XPATH, "//p").text
    print("Paragraph:", paragraph)

    # *3. Extract using CSS Selector*
    image = driver.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
    print("Image Source:", image)

    # *4. Extract using Link Text*
    link = driver.find_element(By.LINK_TEXT, "Code Org")
    print("Link Text:", link.text)
    print("Link URL:", link.get_attribute("href"))

    # *5. Extract multiple elements (find_elements)*
    addresses = driver.find_elements(By.TAG_NAME, "address")
    for address in addresses:
        print("Address:", address.text)

    # *6. Extract using Partial Link Text*
    partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Code")
    print("Partial Link Text:", partial_link.text)

except Exception as e:
    print("Error:", e)

finally:
    # Close browser
    driver.quit()
