# Author: Biscoitinho

import datetime
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.keys import Keys

from random import randrange
import ctypes

# ============================================= Changes these lines =============================================
# The URL for "Senior Sistemas".
SENIOR_LOGIN_URL = "https://platform.senior.com.br/login/?redirectTo=https%3A%2F%2Fplatform.senior.com.br%2Fsenior-x%2F%23%2FGest%25C3%25A3o%2520de%2520Pessoas%2F1%2Fres%3A%252F%252Fsenior.com.br%252Fhcm%252Fpontomobile%252FclockingEvent%3Fcategory%3Dframe%26link%3Dhttps%3A%252F%252Fplatform.senior.com.br%252Fhcm-pontomobile%252Fhcm%252Fpontomobile%252F%2523%252Fclocking-event%26withCredentials%3Dtrue%26r%3D2"
# URL for clock punch.
WEBSITE_CLOCK_PUNCH_URL = "https://platform.senior.com.br/senior-x/#/Favoritos/1/res:%2F%2Fsenior.com.br%2Fhcm%2Fpontomobile%2FclockingEvent?category=frame&link=https:%2F%2Fplatform.senior.com.br%2Fhcm-pontomobile%2Fhcm%2Fpontomobile%2F%23%2Fclocking-event&withCredentials=true&r=0"
# Login e-mail
EMAIL = ''
# Password
PASSWORD = ''
# ============================================= Changes these lines =============================================

# First punch, when you start working.
FIRST_PUNCH = '07:58'
# Second punch, lunch time.
SECOND_PUNCH = '12:00'
# Third punch, coming back from lunch.
THIRD_PUNCH = '12:59'
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

    time.sleep(wait_random_time())
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        browser.get(SENIOR_LOGIN_URL)

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
        browser.quit()
    except Exception as error:
        ctypes.windll.user32.MessageBoxW(0, "A Senior parece estar fora do ar. Você deveria bater o ponto manualmente neste horário.",
         "Ocorreu um erro ao bater o cartão", 1)
        print('Error: ' + str(error))


def wait_random_time():
    random_minutes = [
        0,
        60,
        120,
        180,
    ]
    return random_minutes[randrange(len(random_minutes))]


def current_time():
    return datetime.datetime.now().strftime("%H:%M")


def current_date():
    return datetime.datetime.today().weekday()


if __name__ == "__main__": main()