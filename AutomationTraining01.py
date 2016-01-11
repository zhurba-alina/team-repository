from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class training_01:

    def __init__(self):
        print "Let's start"

    def main(self):
        driver = webdriver.Firefox()

        #try to set implicitly_wait to 4 (button appear delay is 3 seconds)
        driver.implicitly_wait(2)

        driver.maximize_window()
        driver.get("http://php-soflot.rhcloud.com/AutomationTraining01.htm")

        driver.find_element_by_id("a3").click()

        # ----------------
        secondButton = driver.find_element_by_name("2ndButton")
        secondButton.click()
        # see http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
        # comment upper lines, uncomment lines below and watch!
        # ----------------

        # try:
        #     secondButton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "2ndButton")))
        # finally:
        #     secondButton.click()

        final_text = driver.find_element_by_id("finalMission").text
        print ("text = " + final_text)

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    my_app = training_01()
    my_app.main()