import os
import sys
import smtplib
import subprocess
from configobj import ConfigObj
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def send_availability_email (sender, recipient, message):
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipient, message)
    s.quit()

def show_notification (message):
    subprocess.Popen(['notify-send', "Passaporto Online", message])

# Add the selenium drivers to PATH
project_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
config = ConfigObj(project_folder + "/config.ini")
drivers_path = project_folder + "/drivers/" + config["driver"]

# Configure the browser to be headless
options = Options()
options.set_headless()

browser = Chrome(executable_path = drivers_path, options = options)
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
            show_notification("The location " + location_name + " is available")
        else:
            show_notification("The location " + location_name + " is not available")