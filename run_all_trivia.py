"""
Script to run ten KI trivia functions provided by trivia.py
"""
# test git
# install selenium
# download chromdriver and add to path
from selenium import webdriver
import trivia

def pause():
    """
    Asks for user input to continue to the next trivia quiz
    """
    keep_going = '0'
    while keep_going != '1':
        keep_going = input('press 1 to continue: ')


driver = webdriver.Chrome()
trivia.w101_spells(driver)
# pause to login/do captcha, ask for user input to continue
pause()
trivia.w101_wiz_city(driver)
pause()
trivia.w101_adventuring(driver)
pause()
trivia.w101_conjuring(driver)
pause()
trivia.w101_magical(driver)
pause()
trivia.w101_mystical(driver)
pause()
trivia.w101_spellbinding(driver)

# ask for user input to quit webdriver session
quit = '0'
while quit != '1':
    quit = input('press 1 to quit: ')

driver.quit()
