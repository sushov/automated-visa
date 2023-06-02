from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Set up the Chrome driver
# Replace with the path to your Chrome driver
driver = webdriver.Chrome(
    '/Users/beeyond_my_thoughts/desktop/chromedriver_mac64')

# Navigate to the login page
driver.get('https://portal.ustraveldocs.com/')

# Find and check the privacy policy checkbox
# Replace with the actual ID of the privacy policy checkbox
# privacy_checkbox = driver.find_element(By.ID, 'privacy-checkbox')
# privacy_checkbox.click()

privacy_checkboxes = driver.find_elements(
    By.XPATH, '//input[@type="checkbox" and @name="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167"]')

for checkbox in privacy_checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
        break

# Find and fill in the login form
# Replace with the actual ID of the username field
username_field = driver.find_element(
    By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username')
# Replace with the actual ID of the password field
password_field = driver.find_element(
    By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password')
# Replace with the actual ID of the login button
submit_button = driver.find_element(
    By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton')

# Replace 'YourUsername' with your actual username
username_field.send_keys('thapaliyashankar060@gmail.com')
# Replace 'YourPassword' with your actual password
password_field.send_keys('Trishulinadi182@')
submit_button.click()

# Wait for the login to be successful and navigate to the scheduling page
wait = WebDriverWait(driver, 10)
scheduling_link = wait.until(EC.presence_of_element_located(
    (By.ID, 'https://portal.ustraveldocs.com/scheduleappointment')))  # Replace with the actual ID of the scheduling link
scheduling_link.click()

# Wait for the page to load and slots to be displayed
available_slots = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ui-state-default ui-state-active')))

# Extract the available slots
# Replace with the actual class name of the slots
slots = available_slots.find_elements(
    By.CLASS_NAME, 'ui-state-default ui-state-active')

# Check for available slots and find the earliest one before December 2024
earliest_slot = None
for slot in slots:
    slot_date = slot.text.strip()
    slot_datetime = datetime.strptime(slot_date, '%B %d, %Y')
    if slot_datetime < datetime(2024, 12, 1):
        if not earliest_slot or slot_datetime < earliest_slot:
            earliest_slot = slot_datetime

if earliest_slot:
    print(
        f"Earliest available slot before December 2024: {earliest_slot.strftime('%B %d, %Y')}")
    # Add code to perform the rescheduling process
    # Replace with the actual class name of the reschedule button
    reschedule_button = slot.find_element(
        By.CLASS_NAME, 'thePage:SiteTemplate:theForm:addItem')
    reschedule_button.click()
    # Add code to handle the rescheduling process, such as filling in reschedule details and confirming the reschedule
else:
    print("No slots available before December 2024.")

# Close the browser
driver.quit()
