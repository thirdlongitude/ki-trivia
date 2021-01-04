"""
Original file I wrote and tested the script with; automates the W101 Spells Trivia
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# declare dictionary containing questions and corresponding answers
qa_dict = {
    'How many pips does it cost to cast Stormzilla?': '5',
    'What does Forsaken Banshee do?': '375 damage plus a hex trap',
    'Mildred Farseer teaches you what kind of spell?': 'Dispels',
    'Who can teach you the Life Shield Spell?': 'Sabrina Greenstar',
    'Which Fire spell both damages and heals over time?': 'Power Link',
    'What isn\'t a shadow magic spell?': 'Ebon Ribbons',
    'What level of spell does Enya Firemoon Teach?': '80',
    'Ether Shield protects against what?': 'Life and Death attacks',
    'Which spell would not be very effective when going for the elixir vitae Badge?': 'Entangle',
    'Tish\'Mah specializes in spells that mostly affect these:': 'Minions',
    'What type of spells are Ice, Fire, and Storm?': 'Elemental',
    'Mortis can teach you this.': 'Tranquilize',
    'What term best fits Sun Magic Spells?': 'Enchantment',
    'If you\'re a storm wizard with 4 power pips and 3 regular pips, how powerful would your supercharge charm be?': '110%',
    'Which spell can\'t be cast while polymorphed as a Gobbler?': 'Pie in the sky',
    'Cassie the Ponycorn teaches this kind of spell:': 'Prism',
    'How many pips does it cost to cast Dr. Von\'s Monster?': '9',
    'If you can cast Storm Trap, Wild Bolt, Catalan, and the Tempest spell, what are you polymorphed as?': 'Ptera',
    'What term best fits Star Magic Spells?': 'Auras',
    'Who teaches you balance magic?': 'Alhazred'
}

# open the trivia site
driver = webdriver.Chrome()
driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-spells-trivia")

# load jQuery
# with open('jquery-3.5.1.js', errors = 'ignore') as f:
#     driver.execute_script(f.read())

# repeat process 12 times, once for each question
for i in range(12):
    # get question text
    question_text = driver.find_element_by_class_name('quizQuestion').text

    # find corresponding answer from the dictionary and store it in a variable
    answer_text = qa_dict[question_text]
    print(answer_text)

    # find the answer containers
    answer_options = driver.find_elements_by_class_name('answer')

    # loop through the options to find the right answer
    for option in answer_options:
        # when right answer found
        if option.find_element_by_class_name('answerText').get_attribute('textContent').strip() == answer_text:
            # wait for the next button to become visible
            next_button = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('button#nextQuestion.fadeIn'))
            # click on the correct answer
            option.find_element_by_class_name('answerBox').click()
            print('answer clicked')
            break

    # click the next question button
    next_button.click()
    # driver.find_element_by_id('nextQuestion').click()

# click on blue login/see results button
driver.find_element_by_class_name('kiaccountsbuttonblue').click()

# ask for user input to quit webdriver session
quit = '0'
while quit != '1':
    quit = input('press 1 to quit: ')

driver.quit()
