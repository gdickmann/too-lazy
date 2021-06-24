# Author: Biscoitinho

import datetime
import time

from random import randrange

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ============================================= Changes this files =============================================
# The URL for "Senior Sistemas". It can change for each user.
WEBSITE_URL = ""
# Your login e-mail
EMAIL = ''
# Your password
PASSWORD = ''

CHROME_LOCATION = ''
# ============================================= Changes this files =============================================

# First punch, when I start work.
FIRST_PUNCH = '07:55'

# Second punch, lunch time.
SECOND_PUNCH = '11:58'

# Third punch, coming back from lunch.
THIRD_PUNCH = '12:58'

# Last punch.
FOURTH_PUNCH = '17:28'


def main():
    while True:
        check_for_punch(str(current_time()), FIRST_PUNCH)
        check_for_punch(str(current_time()), SECOND_PUNCH)
        check_for_punch(str(current_time()), THIRD_PUNCH)
        check_for_punch(str(current_time()), FOURTH_PUNCH)

        print(current_time(), "isn't time for punch the clock.")
        time.sleep(2)


def check_for_punch(current_time, punch_clock_time):
    if str(current_time) == punch_clock_time:
        print("It's time for punch the clock: " + punch_clock_time)
        do_clock_punch()

        print('Done.')

        # Sleep for 3 minutes, otherwise the check-in will be done each 2 seconds
        # because the current time is still the same.
        time.sleep(180)


def do_clock_punch():
    # Makes invisible tab.
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    try:
        browser = webdriver.Chrome(executable_path=CHROME_LOCATION, chrome_options=options)
        browser.get(WEBSITE_URL)

        print('Waiting...')
        
        # Wait a random time to inaccurate clock punch
        time.sleep(wait_random_time())

        print('Doing the punch...')
        # Login
        browser.find_element_by_css_selector('#username-input-field').send_keys(EMAIL)
        browser.find_element_by_css_selector('#password-input-field').send_keys(PASSWORD)
        browser.find_element_by_css_selector('#loginbtn').send_keys(Keys.ENTER)
        
        time.sleep(5)

        # 'Register time' button
        browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="custom_iframe"]'))
        browser.find_element_by_css_selector('#s-button-1').send_keys(Keys.ENTER)
    except:
        print('Error while trying to punch the clock.')
        main()


def wait_random_time():
    random_minutes = [
        60,
        120,
        140,
        150,
        160,
        170
    ]
    return random_minutes[randrange(len(random_minutes))]


def current_time():
    return datetime.datetime.now().strftime("%H:%M")


if __name__ == "__main__": main()