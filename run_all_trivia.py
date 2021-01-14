"""
Script to run ten KI trivia functions provided by trivia.py
"""
# install selenium
# download chromedriver and add to path
from selenium import webdriver
import trivia

driver = webdriver.Chrome()
# trivia.w101_spells(driver)
# trivia.w101_wiz_city(driver)
# trivia.w101_adventuring(driver)
# trivia.w101_conjuring(driver)
# trivia.w101_magical(driver)
# trivia.w101_mystical(driver)
# trivia.w101_spellbinding(driver)
# trivia.greek_myth(driver)
# trivia.world_capitals(driver)
trivia.book_quotes(driver)

# ask for user input to quit webdriver session
quit = '0'
while quit != '1':
    quit = input('press 1 to quit: ')

driver.quit()
