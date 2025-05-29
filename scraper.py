import json
import time
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_articles():
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the webpage
    url = "https://muzz.com/en-US/blog/relationships/"
    driver.get(url)

    # Wait until articles are loaded
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".hover\\:text-mm-pink"))
        )
    except Exception as e:
        print("Timeout waiting for articles to load:", e)

    # Find articles
    articles = driver.find_elements(By.CSS_SELECTOR, ".hover\\:text-mm-pink")
    extracted_data = []

    for article in articles:
        try:
            titleElement = None
            try:
                titleElement = article.find_element(By.TAG_NAME, "h4")
            except:
                try:
                    titleElement = article.find_element(By.TAG_NAME, "h1")
                except:
                    pass

            thumbnailElement = article.find_element(By.TAG_NAME, "img")
            descriptionElement = article.find_element(By.TAG_NAME, "p")

            extracted_data.append({
                "thumbnail": thumbnailElement.get_attribute("src"),
                "title": titleElement.text if titleElement else "No title",
                "description": descriptionElement.text
            })
        except Exception as e:
            print("Error processing an article:", e)

    # Save to JSON
    output_file = "articles.json"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, indent=4, ensure_ascii=False)

    print(f"Extracted data saved to {output_file}")
    driver.quit()

# Only run when this file is executed directly
if __name__ == "__main__":
    scrape_articles()
