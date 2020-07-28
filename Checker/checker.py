import webbrowser
import random
import os
# from selenium import webdriver


urlList = ['http://www.youtube.com', 'http://www.facebook.com']
url = random.choice(urlList)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
ie_path = 'C:/Program Files/Internet Explorer/iexplore.exe %s'

webbrowser.get(chrome_path).open(url)
webbrowser.get(ie_path).open(url)
#webbrowser.get(ie_path).open(url)

os.startfile('CheckersPowerpoint.pptx')
os.startfile('League of Legends.Lnk')

'''
# Using Chrome to access web
 driver = webdriver.Chrome("C:/Users/michael/Downloads/chromedriver_win32/chromedriver.exe")

# Open the website
driver.get('https://canvas.auckland.ac.nz')

# Select the id box
id_box = driver.find_element_by_name('username')
# Equivalent Outcome! 
id_box = driver.find_element_by_id('username')

# Send id information
id_box.send_keys('my_username')

# Find password box
pass_box = driver.find_element_by_name('password')
# Send password
pass_box.send_keys('my_password')
'''