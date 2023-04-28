from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Instantiate a new Chrome browser
browser = webdriver.Chrome()
time.sleep(2)
# # Navigate to the Notion login page
browser.get("https://www.notion.so/login")
time.sleep(2)

# # Fill in email and password fields
goo_btn = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div",
)
goo_btn.click()
# time.sleep(5)
# browser.get("https://www.notion.so/login")
time.sleep(2)

options = webdriver.ChromeOptions()
# options.add_argument(
#     "--profile-directory=Default"
# )  # use existing Chrome profile for Google login
driver = webdriver.Chrome(options=options)
driver.get("https://www.notion.so/login")

# Click the "Continue with Google" button
google_button = driver.find_element(
    By.XPATH, '//button[@data-analytics-event="Login with Google"]'
)
google_button.click()

# Wait for the Notion dashboard to load
notion_logo = driver.find_element_by_css_selector(".notion-logo")
notion_logo.click()


goo_inp = browser.find_element(
    By.ID,
    "identifierId",
)

goo_inp.send_keys("jacob.crotherz@gmail.com")
goo_btn = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span",
)
goo_btn.click()

sign_btn = browser.find_element(
    By.XPATH, "/html/body/div/div[1]/div/div[3]/div[2]/div[2]/button/div[2]"
)
time.sleep(3)
sign_btn.click()
time.sleep(5)
sel_btn = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[1]/div[1]",
)
time.sleep(3)
sel_btn.click()

time.sleep(3)

con_btn = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[2]",
)
time.sleep(3)

con_btn.click()
time.sleep(3)

sel_btn1 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[2]",
)
sel_btn1.click()

sel_btn1 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div",
)
sel_btn1.click()


sel_btn2 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[4]",
)
sel_btn2.click()

sel_btn2 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div",
)
sel_btn2.click()

sel_btn3 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[6]",
)
sel_btn3.click()

sel_btn3 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div",
)
sel_btn3.click()

sel_btn4 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[8]",
)
sel_btn4.click()

sel_btn4 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div[2]/div",
)
sel_btn4.click()


sel_btn5 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[3]/div/div/div[1]",
)
sel_btn5.click()


work_spa = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[3]/input",
)
work_spa.send_keys("test")

sel_btn6 = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div[2]/div/div[5]",
)
sel_btn6.click()
time.sleep(5)
# Click the submit button
submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(2)

# Close the browser
