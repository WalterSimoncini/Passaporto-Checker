import os
import sys
from configobj import ConfigObj
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

creds = ConfigObj("creds.ini")

# Add the selenium drivers to PATH
project_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
drivers_path = project_folder + "/drivers/chromedriver"

browser = Chrome(executable_path=drivers_path)
browser.get('https://www.passaportonline.poliziadistato.it/logInCittadino.do')

codice_fiscale_textfield = browser.find_element_by_xpath("//*[@id=\"codiceFiscale\"]")
codice_fiscale_textfield.send_keys("123456")

password_textfield = browser.find_element_by_xpath("//*[@id=\"password\"]")
password_textfield.send_keys("123456")

submit_button = browser.find_element_by_xpath("//*[@id=\"btnSub\"]")
# submit_button.submit()