from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

# Set up logging
logging.basicConfig(filename='amazon_automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

# Create directory for screenshots
screenshot_dir = 'screenshots'
os.makedirs(screenshot_dir, exist_ok=True)

def save_screenshot(step_name):
    screenshot_path = os.path.join(screenshot_dir, f'{step_name}.png')
    driver.save_screenshot(screenshot_path)
    logging.info(f'Screenshot saved: {step_name}')

try:
    # Step 1: Go to Amazon India
    try:
        driver.get("https://www.amazon.in/")
        assert "Amazon" in driver.title
        logging.info("Opened Amazon India")
        save_screenshot('step_1_homepage')
    except Exception as e:
        logging.error(f"Step 1 failed: {e}")
        save_screenshot('step_1_error')
        raise e

    # Step 2: Search for 'mobile'
    try:
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("mobile", Keys.RETURN)
        logging.info("Searched for 'mobile'")
        save_screenshot('step_2_search')
    except Exception as e:
        logging.error(f"Step 2 failed: {e}")
        save_screenshot('step_2_error')
        raise e

    # Step 3: Apply 4-star filter
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='a-icon a-icon-star-medium a-star-medium-4']"))
        ).click()
        logging.info("Applied 4-star filter")
        save_screenshot('step_3_filter')
    except Exception as e:
        logging.error(f"Step 3 failed: {e}")
        save_screenshot('step_3_error')
        raise e

    # Step 4: Set price range ₹10,000 - ₹20,000
    try:
        driver.get(
            "https://www.amazon.in/s?k=mobile&crid=1I1F2B7PGKJSV&qid=1725027060&rnid=1318502031&sprefix=mobil%2Caps%2C206&ref=sr_nr_p_36_0_0&low-price=10000&high-price=20000"
        )
        time.sleep(3)
        logging.info("Price range set")
        save_screenshot('step_4_price_range')
    except Exception as e:
        logging.error(f"Step 4 failed: {e}")
        save_screenshot('step_4_error')
        raise e

    # Step 5: Open first product
    try:
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]//h2/a"))
        )
        first_product_link = first_result.get_attribute('href')
        driver.execute_script(f"window.open('{first_product_link}');")
        driver.switch_to.window(driver.window_handles[1])
        logging.info("First product opened")
        save_screenshot('step_5_open_product')
    except Exception as e:
        logging.error(f"Step 5 failed: {e}")
        save_screenshot('step_5_error')
        raise e

    # Step 6: Add product to cart
    try:
        add_to_cart_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button']"))
        )
        add_to_cart_button.click()

        go_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='a-button-input']"))
        )
        go_to_cart_button.click()
        time.sleep(3)
        logging.info("Product added to cart")
        save_screenshot('step_6_add_to_cart')
    except Exception as e:
        logging.error(f"Step 6 failed: {e}")
        save_screenshot('step_6_error')
        raise e

except Exception as e:
    logging.error(f"An error occurred: {e}")
    save_screenshot('final_error')

finally:
    # Close the browser
    driver.quit()
    logging.info("Browser closed")
