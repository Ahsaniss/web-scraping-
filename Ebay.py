from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Initialize driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    url = 'https://www.ebay.com/b/Bed-Sheets/20460/bn_2312175'
    print(f"Loading URL: {url}")
    driver.get(url)

    # Wait for page to load completely
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".b-list__items_nofooter"))
    )
    print("Page loaded successfully")

    # Get all product items
    items = driver.find_elements(By.CSS_SELECTOR, "li.s-item")[:10]  # First 10 items

    scraped_data = []

    for item in items:
        data = {
            'title': 'N/A',
            'price': 'N/A',
            'rating': 'N/A',
            'category': 'N/A'
        }

        try:
            data['title'] = item.find_element(By.CSS_SELECTOR, ".s-item__title span").text.strip()
        except:
            pass

        try:
            data['price'] = item.find_element(By.CSS_SELECTOR, ".s-item__price").text.strip()
        except:
            pass

        try:
            rating_element = item.find_element(By.CSS_SELECTOR, ".x-star-rating span")
            data['rating'] = rating_element.get_attribute("aria-label").replace("out of 5 stars", "").strip()
        except:
            pass

        try:
            data['category'] = item.find_element(By.CSS_SELECTOR, ".s-item__dynamic:last-child").text.strip()
        except:
            pass

        scraped_data.append(data)

    # Display results
    for idx, product in enumerate(scraped_data, 1):
        print(f"\nProduct #{idx}")
        print(f"Title: {product['title']}")
        print(f"Price: {product['price']}")
        print(f"Rating: {product['rating']}/5")
        print(f"Category: {product['category']}")
        print("-" * 60)

except Exception as e:
    print(f"\nError occurred: {str(e)}")

finally:
    driver.quit()
    print("\nBrowser closed")