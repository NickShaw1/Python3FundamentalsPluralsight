import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate WebDriver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get("https://the-internet.herokuapp.com/inputs")

# Wait for the input field to be visible
input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
)

# Enter data into the input field
input_field.send_keys("99")  # Example: Enter value "101"

# Add a wait to keep the browser open
time.sleep(5)  # Adjust the sleep time as needed

# Print the value of the input field
input_value = input_field.get_attribute("value")
print("Value of the input field:", input_value)

# Check if the value is greater than 100
if int(input_value) > 100:
    print("Error - More than 100 was entered")

# Close the browser
driver.quit()
