import os
import sys
from configobj import ConfigObj
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

config = ConfigObj("config.ini")

# Add the selenium drivers to PATH
project_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
drivers_path = project_folder + "/drivers/" + config["driver"]

browser = Chrome(executable_path=drivers_path)
browser.get('https://www.passaportonline.poliziadistato.it/logInCittadino.do')

# Login to the portal
codice_fiscale_textfield = browser.find_element_by_xpath("//*[@id=\"codiceFiscale\"]")
codice_fiscale_textfield.send_keys(config["codice_fiscale"])

password_textfield = browser.find_element_by_xpath("//*[@id=\"password\"]")
password_textfield.send_keys(config["password"])

submit_button = browser.find_element_by_xpath("//*[@id=\"btnSub\"]")
submit_button.submit()

# Search for availability
search_button = browser.find_element_by_xpath("//*[@id=\"CittadinoForm\"]/fieldset/input")
search_button.click()

# Find available locations
locations = browser.find_elements_by_class_name('data')

for l in locations:
    fields = l.find_elements_by_tag_name("td")

    location_name = fields[0].text
    location_availability = fields[5].text.lower()

    if config["location"] in location_name.lower():
        if location_availability != "no":
            print "Location available"