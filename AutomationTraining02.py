from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class training_01:

    def __init__(self):
        print "Let's start"

    def main(self):
        upload_file_path = (os.path.dirname(__file__) + "/values.txt")
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

        driver.maximize_window()
        driver.get("http://php-soflot.rhcloud.com/AutomationTraining02_startUpload.php")

        print ("attempting to upload file " + upload_file_path)
        print ("But seems like on Winsows we need to use windows-style slashes - backslashes!")
        upload_file_path = upload_file_path.replace("/", "\\")

        print ("now upload file path is " + upload_file_path)

        driver.find_element_by_name("AutomationTraining02file").send_keys(upload_file_path)
        driver.find_element_by_xpath("//input[3]").click()

        # ----------------
        final_text = driver.find_element_by_xpath("//body/div").text
        print ("file processing result = " + final_text)

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    my_app = training_01()
    my_app.main()