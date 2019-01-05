import os
import sys
import smtplib
import subprocess
from configobj import ConfigObj
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
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

# Configure the browser to be headless
chrome_options = ChromeOptions()
# Disabling the sandboxing is needed in order to avoid crashes in the Docker container
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

browser = Chrome(chrome_options = chrome_options, executable_path = "/usr/local/bin/chromedriver")
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
            print("The location " + location_name + " is available")
        else:
            print("The location " + location_name + " is not available")