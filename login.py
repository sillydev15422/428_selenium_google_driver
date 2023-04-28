from undetected_chromedriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


class Google:
    def __init__(self) -> None:
        self.url = "https://accounts.google.com/v3/signin/identifier?dsh=S-1442831692%3A1682626769754259&continue=https%3A%2F%2Fdrive.google.com%2F&emr=1&followup=https%3A%2F%2Fdrive.google.com%2F&ifkv=AQMjQ7SeZCit4xy3wyMZ_PiVHCEQZuKjPip37Gr8x34r_zuqsjTDHwocgkhF9nuc3fbxG77MPeaHZw&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        self.driver = Chrome(use_subprocess=True)
        self.driver.get(self.url)
        self.time = 10

    def login(self, email, password):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "identifier"))
        ).send_keys(f"{email}\n")
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "Passwd"))
        ).send_keys(f"{password}\n")

        self.code()

    def code(self):
        # [ ---------- paste your code here ---------- ]
        time.sleep(self.time)
        self.get_documents()
        self.get_notion_documents()

    def get_documents(self):
        self.driver.get("https://drive.google.com/drive/my-drive")
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.send_keys("resume")
        print("123")
        time.sleep(2)
        searchButton = self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[2]/header/div[2]/div[2]/div[2]/form/button[4]",
        )
        searchButton.click()
        time.sleep(2)
        #########################

        lisButton = self.driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[5]/div[2]/div[2]/div/c-wiz/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[1]",
            #
        )
        lisButton.click()
        time.sleep(14)

        download_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[2]/div[5]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[5]",
        )
        download_button.click()

        # save_to_drive_button = self.driver.find_element(
        #     By.XPATH, '//div[@aria-label="Save to Drive"]'
        # )

        download_dir = os.path.expanduser("~/Documents/DocumentBackups")
        print("sdfsdfsd")
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        filename = "test.txt"
        print("123123")
        # save_to_drive_button.click()
        # save_button = self.driver.find_element(By.XPATH, '//button[text()="Save"]')
        # save_button.click()
        # Wait for download to complete
        # while not any(
        #     fname.endswith(".crdownload") for fname in os.listdir(download_dir)
        # ):
        # time.sleep(1)
        # Rename the downloaded file
        os.rename(
            os.path.join(download_dir, filename),
            os.path.join(download_dir, "test_backup.txt"),
        )
        # for link in self.driver.find_elements(By.XPATH, '//a[@class="doc-title-link"]'):
        #     print(link)
        #     href = link.get_attribute("href")
        #     filename = link.text + ".txt"  # use document title as filename
        #     download_dir = "/path/to/local/backup/folder"
        #     if not os.path.exists(download_dir):
        #         os.makedirs(download_dir)
        #     self.driver.execute_script("window.open()")
        #     self.driver.switch_to.window(self.driver.window_handles[-1])
        #     self.driver.get(href)
        #     text = self.driver.find_element_by_xpath(
        #         "//pre"
        #     ).text  # extract text from document
        #     with open(os.path.join(download_dir, filename), "w") as f:
        #         f.write(text)
        #     self.driver.close()
        #     self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(100)

    def get_notion_documents(self):
        self.driver.get()


if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = "webdev.0220@gmail.com"  # replace email
    password = "senko438"  # replace password
    #  ---------- EDIT ----------

    google = Google()
    google.login(email, password)
