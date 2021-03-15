"""
Module that provides functions to run KingsIsle trivia quizzes
"""
from selenium.webdriver.support.ui import WebDriverWait
import sys
# does most of the work
def fill_answers(driver, qa_dict):
    """
    Fills in answers for the current trivia quiz using the qa_dict given.
    """
    # repeat process 12 times, once for each question
    for i in range(12):
        # get question text
        question_text = driver.find_element_by_class_name('quizQuestion').text
        ## print(question_text)

        # find corresponding answer from the dictionary and store it in a variable
        answer_text = qa_dict[question_text]

        # find the answer containers
        answer_options = driver.find_elements_by_class_name('answer')

        # loop through the options to find the right answer
        for option in answer_options:
            # get option text
            option_text = option.find_element_by_class_name('answerText').get_attribute('textContent').strip()
            # when right answer found
            if answer_text == option_text:
                # wait for the next button to become visible
                next_button = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('button#nextQuestion.fadeIn'))
                # click on the correct answer
                option.find_element_by_class_name('answerBox').click()
                ## print('checked box ' + str(i + 1))
                break

        # click the next question button
        ## print('clicking next ' + str(i + 1))
        next_button.click()
        ## print('clicked next')

    # click on blue login/see results button
    driver.find_element_by_class_name('kiaccountsbuttonblue').click()

def pause(driver):
    """
    Asks for user input. If input is 1, continue to the next trivia quiz; if input is 2, quit the program.
    """
    keep_going = '0'
    while keep_going != '1' and keep_going != '2':
        keep_going = input('press 1 to continue or 2 to quit: ')
        if keep_going == '2':
            driver.quit()
            sys.exit()

def w101_spells(driver):
    """
    Autofills the W101 Spells Trivia
    """
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
    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-spells-trivia")
    # call function to actually do the quiz
    fill_answers(driver, qa_dict)
    # pause to login/do captcha, ask for user input to continue
    pause(driver)

def w101_wiz_city(driver):
    """
    Autofills the W101 Wizard City Trivia
    """
    qa_dict = {
        'What are the main colors for the Myth School?': 'Blue and Gold',
        'What are the school colors of Balance?': 'Tan and Maroon',
        'What does every Rotting Fodder in the Dark Caves carry with them?': 'A spade',
        'What is Diego\'s full name?': 'Diego Santiago Quariquez Ramirez the Third',
        'What is Mindy\'s last name (she\'s on Colossus Blvd)?': 'Pixiecrown',
        'What is something that the Gobblers are NOT stockpiling in Colossus Way?': 'Broccoli',
        'What is the gemstone for Balance?': 'Citrine',
        'What is the name of the bridge in front of the Cave to Nightside?': 'Rainbow Bridge',
        'What is the name of the grandfather tree?': 'Bartleby',
        'What is the name of the Ice Tree in Ravenwood?': 'Kelvin',
        'What is the name of the school newspaper? Boris Tallstaff knows...': 'Ravenwood Bulletin',
        'What school does Malorn Ashthorn think is the best?': 'Death',
        'What school is all about Creativity?': 'Storm',
        'Where is Sabrina Greenstar?': 'Fairegrounds',
        'Who is the Fire School professor?': 'Dalia Falmea',
        'Who is the Princess of the Seraphs?': 'Lady Oriel',
        'Who is the Wizard City mill foreman?': 'Sohomer Sunblade',
        'Who resides in the Hedge Maze?': 'Lady Oriel',
        'Who sang the Dragons, Tritons and Giants into existance?': 'Bartleby',
        'Who taught Life Magic before Moolinda Wu?': 'Sylvia Drake'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-wizard-city-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def w101_adventuring(driver):
    """
    Autofills the W101 Adventuring Trivia
    """
    qa_dict = {
        # not the right answer for following question; should be '900 � 1000 Fire Damage + 300 Fire Damage to entire team'
        # workaround because click() doesn't work on the right answer for some reason
        'An unmodified Sun Serpent does what?': '440 + 351 Fire Damage over 3 Rounds to entire team',
        'How long do you have to wait to join a new match after fleeing in PVP?': '5 minutes',
        'In Grizzleheim, the Ravens want to bring about:': 'The Everwinter, to cover the world in ice:',
        'Shaka Zebu is known best as:': 'The Greatest Living Zebra Warrior',
        'Who is in the top level of the Tower of the Helephant?': 'Lyon Lorestriker',
        'What determines the colors of the manders in Krok?': 'Where they come from and their school of focus.',
        'What is the name of the new dance added with Khrysalis?': 'The bee dance',
        'What is unique about Falmea\'s Classroom?': 'There are scorch marks on the ceiling',
        'What is Professor Falmea\'s favorite food?': 'Pasta Arrabiata',
        'Which of these are not a lore spell?': 'Fire Dragon',
        'What is the name of the book stolen from the Royal Museum?': 'The Krokonomicon',
        'What school is the Gurtok Demon focused on?': 'Balance',
        'What school is the spell Dark Nova': 'Shadow',
        'What does the Time Ribbon Protect against?': 'Time Flux',
        'What type of rank 8 spell is granted to Death students at level 58?': 'Damage + DoT',
        'What hand does Lady Oriel hold her wand in?': 'Trick question, she has a sword.',
        'Which Aztecan ponders the Great Questions of Life?': 'Philosoraptor',
        'Which of these is NOT a Zafaria Anchor Stone?': 'Rasik Anchor Stone',
        'Who is the Bear King of Grizzleheim?': 'Valgard Goldenblade',
        'What is the name of the secret society in Krokotopia': 'Order of the Fang'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-adventuring-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def w101_conjuring(driver):
    """
    Autofills the W101 Conjuring Trivia
    """
    qa_dict = {
        'What was the name of the powerful Grendel Shaman who sealed the runic doors?': 'Thulinn',
        'Who is the King of the Burrowers?': 'Pyat MourningSword',
        'What did Abigail Dolittle accuse Wadsworth of stealing?': 'Genuine Imitation Golden Ruby',
        'What book was Anna Flameright accused of stealing?': 'Advanced Flameology',
        'Who Is NOT a member of the Council of Light?': 'Cyrus Drake',
        'Kirby Longspear was once a student of which school of magic?': 'Death',
        'Sir Edward Halley is the Spiral\'s most famous:': 'Aztecosaurologist',
        'Who is Bill Tanner\'s sister?': 'Sarah Tanner',
        'What level must you be to wear Dragonspyre crafted clothing?': '33',
        'How many portal summoning candles are in the Burial Mound?': 'Three',
        'What is the shape on the weather vanes in the Shopping District?': 'Half moon/moon',
        'Which Queen is mentioned in the Marleybone book "The Golden Age"?': 'Ellen',
        'The Swordsman Destreza was killed by:': 'A Gorgon'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-conjuring-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def w101_magical(driver):
    """
    Autofills the W101 Magical Trivia
    """
    qa_dict = {
        'Who is the Registrar of Pigswick Academy?': 'Mrs. Dowager',
        'Who guards the entrance to Unicorn Way?': 'Private Stillson',
        'How many worlds of The Spiral are unlocked as of May 21st, 2014?': '12',
        'What is the shape of the pink piece in potion motion?': 'Heart',
        'What can be used to diminish the Nirini\'s powers in Krokotopia?': 'Flame Gems',
        'What color is the door inside the boys dormroom?': 'Red',
        'What\'s the name of the balance tree?': 'Niles',
        'Who prophesizes this? "The mirror will break, The horn will call, From the shadows I strike , And the skies will fall..."': 'Morganthe',
        'Why are the pixies and faeries on Unicorn Way evil?': 'Rattlebones corrupted them.',
        'Zafaria is home to what cultures?': 'Gorillas, Zebras, Lions',
        'Which one of these are not a symbol on the battle sigil?': 'Wand',
        'Who sells Valentine\'s Day items in Wizard City?': 'Valentina Heartsong',
        'What is the title of the book that is floating around the Wizard City Library?': 'Basic Wizarding & Proper Care of Familiars',
        'What book does Professor Drake send you to the library to check out?': 'Book on the Wumpus',
        'Who is the Nameless Knight?': 'Sir Malory',
        'Which is the only school left standing in Dragonspyre?': 'Fire',
        'Merle Ambrose is originally from which world?': 'Avalon',
        'What did Prospector Zeke lose track of in MooShu?': 'Blue Oysters',
        'Which below are NOT a type of Oni in MooShu?': 'Ruby',
        'Why are the Gobblers so afraid to go home?': 'Witches',
        'Which of these locations is not in Wizard City?': 'Digmore Station'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-magical-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def w101_mystical(driver):
    """
    Autofills the W101 Mystical Trivia
    """
    qa_dict = {
        'Hrundle Fjord is part of what section of Grizzleheim?': 'Wintertusk',
        'Who is the Emperor of Mooshu\'s Royal Guard?': 'Noboru Akitame',
        'Who gives you permission to ride the boat to the Krokosphinx?': 'Sergent Major Talbot',
        'What is used to travel to the Isle of Arachnis?': 'Ice Archway',
        'King Neza is Zenzen Seven Star\'s:?': 'Grandfather',
        'Who takes you across the River of Souls?': 'Charon',
        'In Reagent\'s Square, the Professor is standing in front of a:': 'Telegraph Box',
        'Who did Falynn Greensleeves fall in love with?': 'Sir Malick de Logres',
        'Where is the only pure fire in the Spiral found?': 'Wizard City',
        'Who asks you to find Khrysanthemums?': 'Eloise Merryweather',
        'King Axaya Knifemoon needs what to unify the people around him?': 'The Badge of Leadership',
        'Who was ordered to guard the Sword of Kings?': 'The Knights of the Silver Rose',
        'Who is the only person who knows how to enter the Tomb of Storms?': 'Hetch Al\'Dim',
        'Which villain terrorizes the fair maidens of Marleybone?': 'Jaques the Scatcher',
        'In what world would you find the Spider Temple': 'Zafaria',
        'Thaddeus Price is the Pigswick Academy Professor of what school?': 'Tempest',
        'Who was the greatest Aquilan Gladiator of all time?': 'Dimachaerus',
        'What was Ponce de Gibbon looking for in Azteca?': 'The Water of Life',
        'Who haunts the Night Warrens?': 'Nosferabbit',
        'Who tells you how to get to Aquila?': 'Harold Argleston'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-mystical-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def w101_spellbinding(driver):
    """
    Autofills the W101 Spellbinding Trivia
    """
    qa_dict = {
        'Who tells you to speak these words only unto your mentor: "Meena Korio Jajuka!"': 'Priya the Dryad',
        'Who grants the first Shadow Magic spell?': 'Sophia DarkSide',
        'Who taunts you with: "Prepare to be broken, kid!"': 'Clanker',
        'Morganthe got the Horned Crown from the Spriggan:': 'Gisela',
        'Who needs the healing potion from Master Yip?': 'Binh Hoa',
        'Who is Haraku Yip\'s apprentice?': 'Binh Hoa',
        'What does Silenus name you once you\'ve defeated Hades?': 'Glorious Golden Archon',
        'Who tells you: "A shield is just as much a weapon as the sword."': 'Mavra Flamewing',
        'Who taunts: Why I oughta knock you to the moon, you pesky little creep!': 'Mugsy',
        'Sumner Fieldgold twice asks you to recover what for him?': 'Shrubberies',
        'What special plant was Barley developing in his Garden?': 'Cultivated Woodsmen',
        'Who tries to raise a Gorgon Army?': 'Phorcys',
        'What badge do you earn by defeating 100 Samoorai?': 'Yojimbo',
        'Where has Pharenor been imprisoned?': 'Skythorn Tower',
        'Who makes the harpsicord for Shelus?': 'Gretta Darkkettle',
        'Who taunts you with: "Wizard, you will know the meaning of the word pain after we battle!"': 'Aiuchi',
        'In Azteca, Morganthe enlisted the help of the:': 'The Black Sun Necromancers',
        'Who thinks you are there to take their precious feathers?': 'Takeda Kanryu',
        'The Swallows of Caliburn migrate to Avalon from where each year?': 'Zafaria and Marleybone',
        'Who helps Morganthe find the Horn of Huracan?': 'Belloq'
    }

    driver.get("https://www.wizard101.com/quiz/trivia/game/wizard101-spellbinding-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def greek_myth(driver):
    """
    Autofills the Greek Mythology Trivia
    """
    qa_dict = {
        'Which Greek god is the god of music, healing, light and truth?': 'Apollo',
        'Which Greek god is the goddess of springtime?': 'Persephone',
        'Which Greek god is the goddess of corn, grain and harvest?': 'Demeter',
        'Which Greek god is the goddess of marriage and childbirth?': 'Hera',
        'Which Greek is the sun titan?': 'Helios',
        'Which Greek god is the god of war?': 'Ares',
        'Which Greek god is the god of love?': 'Eros',
        'Which Greek god is the ruler of the Olympian gods?': 'Zeus',
        'Which Greek god is the goddess of discord?': 'Eris',
        'Which Greek god is the god of fire and forge?': 'Hephaestus',
        'Which Greek god is the lord of the underworld?': 'Hades',
        'Which Greek god is the goddess of intelligence and the arts?': 'Athena',
        'Which Greek god is the god of flocks and shepherds?': 'Pan',
        'Which Greek god is the personification of death?': 'Thanatos',
        'Which Greek god is the god of fertility and wine?': 'Dionysus',
        'Which Greek god is the protector of all waters?': 'Poseidon',
        'Which Greek god is the goddess of youth?': 'Hebe',
        'Which Greek god is the goddess of love, desire and beauty?': 'Aphrodite',
        '': '', '': '', '': '', '': ''
        }

    driver.get("https://www.wizard101.com/quiz/trivia/game/greek-mythology-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def world_capitals(driver):
    """
    Autofills the World Capitals Trivia
    """
    qa_dict = {
        'What is the capital of Brazil?': 'Brasilia',
        'What is the capital of Italy?': 'Rome',
        'What is the capital of Mexico?': 'Mexico City',
        'What is the capital of Germany?': 'Berlin',
        'What is the capital of Argentina?': 'Buenos Aires',
        'What is the capital of The Bahamas?': 'Nassau',
        'What is the capital of Egypt?': 'Cairo',
        'What is the capital of Austria?': 'Vienna',
        'What is the capital of Canada?': 'Ottawa',
        'What is the capital of Japan?': 'Tokyo',
        'What is the capital of Czech Republic?': 'Prague',
        'What is the capital of Greece?': 'Athens',
        'What is the capital of Denmark?': 'Copenhagen',
        'What is the capital of India?': 'New Delhi',
        'What is the capital of Belgium?': 'Brussels',
        'What is the capital of Finland?': 'Helsinki',
        'What is the capital of Cuba?': 'Havana',
        'What is the capital of Hungary?': 'Budapest',
        'What is the capital of China?': 'Beijing',
        'What is the capital of Australia?': 'Canberra',
        'What is the capital of France?': 'Paris'
        }

    driver.get("https://www.wizard101.com/quiz/trivia/game/world-capitals-trivia")
    fill_answers(driver, qa_dict)
    pause(driver)

def book_quotes(driver):
    """
    Autofills the Book Quotes Trivia
    """
    qa_dict = {
        '"Call me Ishmael."': 'Moby Dick',
        '"I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous."': 'Frankenstein',
        '"All grown-ups were once children - but only few of them remember it."': 'The Little Prince',
        '"Most people were heartless about turtles because a turtle\'s heart will beat for hours after it has been cut up and butchered. But the old man thought, I have such a heart too."': 'The Old Man and the Sea',
        '"Anything worth dying for is certainly worth living for."': 'Catch-22',
        '"All animals are equal, but some animals are more equal than others."': 'Animal Farm',
        '"The sky above the port was the color of television, tuned to a dead channel."': 'Neuromancer',
        '"Not all those who wander are lost."': 'The Lord of the Rings',
        '"I have been bent and broken, but - I hope - into a better shape."': 'Great Expectations',
        '"Don\'t ever tell anybody anything. If you do, you start missing everybody."': 'The Catcher in the Rye',
        '"You don\'t know about me without you have read a book by the name of \'The Adventures of Tom Sawyer\'; but that ain\'t no matter. That book was made by a Mr Mark Twain, and he told the truth, mainly."': 'The Adventures of Huckleberry Finn',
        '"In spite of everything I still believe that people are really good at heart"': 'The Diary of Anne Frank',
        '"I\'m not afraid of storms, for I\'m learning how to sail my ship."': 'Little Women',
        '"I wanted you to see what real courage is, instead of getting the idea that courage is a man with a gun in his hand. It\'s when you know you\'re licked before you begin but you begin anyway and you see it through no matter what."': 'To Kill a Mockingbird',
        '"It was a pleasure to burn."': 'Farenheit 451',
        '"It is to the credit of human nature that, except where its selfishness is brought into play, it loves more readily than it hates."': 'The Scarlet Letter'
        }

    driver.get("https://www.wizard101.com/quiz/trivia/game/book-quotes-trivia")
    fill_answers(driver, qa_dict)
