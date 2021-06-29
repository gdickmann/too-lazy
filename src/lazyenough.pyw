# Author: Biscoitinho

import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import sys

# ============================================= Changes this files =============================================
# The URL for "Senior Sistemas". It can change for each user.
WEBSITE_LOGIN_URL = ""
WEBSITE_CLOCK_PUNCH_URL = ""
# Your login e-mail
EMAIL = ''
# Your password
PASSWORD = ''

CHROME_LOCATION = 'C:/chromedriver.exe'
# ============================================= Changes this files =============================================

# First punch, when I start work.
FIRST_PUNCH = '8:00'
# Second punch, lunch time.
SECOND_PUNCH = '12:00'
# Third punch, coming back from lunch.
THIRD_PUNCH = '13:00'
# Last punch.
FOURTH_PUNCH = '17:00'

SATURDAY = 5
SUNDAY = 6

def main():
    while True:        
        if is_weekday(current_date()):
            check_for_punch(str(current_time()), FIRST_PUNCH)
            check_for_punch(str(current_time()), SECOND_PUNCH)
            check_for_punch(str(current_time()), THIRD_PUNCH)
            check_for_punch(str(current_time()), FOURTH_PUNCH)

            print(current_time(), "isn't time for punch the clock.")
            time.sleep(2)
        else:
            print("Isn't week day!")
            time.sleep(2)


def check_for_punch(current_time, punch_clock_time):
    if str(current_time) == punch_clock_time:
        print("It's time for punch the clock: " + punch_clock_time)
        do_clock_punch()

        print('Done.')

        # Sleep for 3 minutes, otherwise the clock punch will be done each 2 seconds
        # because the current time is still the same.
        time.sleep(180)


def is_weekday(day_of_week):
    return day_of_week != SATURDAY and day_of_week != SUNDAY


def do_clock_punch():
    # Makes invisible tab.
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    try:
        browser = webdriver.Chrome(executable_path=CHROME_LOCATION, chrome_options=options)
        browser.get(WEBSITE_LOGIN_URL)

        print('Doing the punch...')
        # Login
        browser.find_element_by_css_selector('#username-input-field').send_keys(EMAIL)
        browser.find_element_by_css_selector('#password-input-field').send_keys(PASSWORD)
        browser.find_element_by_css_selector('#loginbtn').send_keys(Keys.ENTER)

        time.sleep(3)
        
        browser.get(WEBSITE_CLOCK_PUNCH_URL)

        time.sleep(15)

        browser.switch_to.frame(browser.find_element_by_css_selector('#custom_iframe'))
        # 'Register time' button
        browser.find_element_by_css_selector('#s-button-1').send_keys(Keys.ENTER)

        time.sleep(3)

        browser.close()
    except Exception as error:
        print(str(error))


def current_time():
    return datetime.datetime.now().strftime("%H:%M")


def current_date():
    return datetime.datetime.today().weekday()


if __name__ == "__main__": main()