


"""
Title: Scraping Demo
Author: Will Sims
Python runs in the terminal, I'll probably have to help you
setup running a Python script. Its hard to explain with text.
But if you have installed Python and its in your environment
variables PATH, you should be able to type "python scraper.py"
in order to run this. If not, i'll help you soon.
Python is also white space sensitive. That means that there are no opening
and closing brackets for blocks of code. If you indent something, Python
assumes that is a new block of code. The only example of this in this file
is the for loop i wrote at the bottom. The for loop only works because I indented
the print statement right below the for loop declaration. I hope that makes sense haha.
To read more about the package we're using to scrape,
Google "python selenium". Any line that starts with a
"#" means its a comment. So this file only has like 5 lines of real code.
"""




# These are imports packages. You only import things that you need.
# There are packages for all kinds of stuff (Regressions, Scraping, Time,
#	complicated math, etc.). But for this scraper, we only need a few selenium packages.

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver



driver = webdriver.Chrome() # Opens a chrome browser to scrape with
driver.get("http://will-sims.com") # Tells the Chrome browser to go to this URL


# (I addded the BEFORE, AFTER, & '-------' just to make the separation clearer
# 	when it is printed in the terminal)
print "BEFORE PAGE SOURCE"
print driver.page_source.encode('utf-8') # This command prints the entire HTML string of the page you're on
print "AFTER PAGE SOURCE"
print "----------------------------------------------"


# Other than searching through the giant string in 'driver.page_source',
# 	there are a few different ways to get data from a page. You have
# 	to target certain elements on the page. If you right click any browser and
# 	click "Inspect", you can see the elements that im talking about. If you
# 	right-click an element in the dev tools, you can "copy Xpath". The XPATH is
# 	USUALLY how I like to locate elements on a page. But you can target elements via
# 	ID, class name, the inner text, etc.


# Here I create a variable (of type WebElement), in order to
# 	get the text out of it, you just type "header_element_of_my_website.text")
header_element_of_my_website = driver.find_element_by_xpath('//*[@id="about_me_with_headshot"]/h2')

# Printing will show the text you want to print in the terminal window
# I use it ALL of the time
print header_element_of_my_website.text

###############################################################
#### Now if you want to grab mmultiple elements on a page #####
###############################################################

all_skills_I_have_that_are_at_bottom_of_my_website = driver.find_elements_by_xpath('//*[@id="skills"]/div/ul/div/li/a')


# This is a for loop. I think you used them a little bit with R
# 	in one of your analytics classes. This just means for every item in a list,
# 	print it.

number_of_skills = 0

for skill_element in all_skills_I_have_that_are_at_bottom_of_my_website:
	print skill_element.text
	number_of_skills = number_of_skills + 1

# You can't directly print integers to the terminal so you have to use
# the str() method to convert them to strings.

# The curly brackets in the middle of the string represent a placeholder
# 	for the .format() method. Whatever you put inside of the .format()
# 	parenthesis is what will be put where the curly brackets are.

print "WOW! Will is some sort of coding God! He has {} skills! Wow! Just Wow!".format(str(number_of_skills))

