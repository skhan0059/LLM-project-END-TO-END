from bs4 import BeautifulSoup
import requests


# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def fetch_website_contents(url):
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    text = driver.find_element(By.TAG_NAME, "body").text
    driver.quit()

    return {
        "url": url,
        "content": text[:3000],  # limit like before
        "error": None
    }



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin

def fetch_website_links(url):
    """
    Return all links on the website at the given URL using Selenium.
    Handles JavaScript-rendered pages, ensures absolute URLs,
    and filters out empty or invalid links.
    """
    
    # Start a Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Extract <a href="..."> elements
    elements = driver.find_elements(By.TAG_NAME, "a")

    links = []
    for elem in elements:
        href = elem.get_attribute("href")
        if href:
            # Convert relative URLs to absolute
            absolute = urljoin(url, href)
            links.append(absolute)

    driver.quit()

    # Remove duplicates
    links = list(set(links))

    return links


