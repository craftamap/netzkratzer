from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def await_element_present(driver, css_selector: str, timeout=10):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def main():
    with webdriver.Firefox(executable_path="./geckodriver") as driver:
        driver.get("https://www.reddit.com/r/all/")
        elements = driver.find_elements_by_css_selector("img")
        img: WebElement
        for img in elements:
            print(img.get_attribute("src"))


if __name__ == "__main__":
    main()