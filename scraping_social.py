# speech recognition module
import speech_recognition as sr
# import pyaudio or else ith will throw an audio processing error
import pyaudio
# import selenium for web scraping
from selenium import webdriver
# import this selenium web driver module for finding elements by tag-name, class etc..
from selenium.webdriver.common.by import By
# Inorder to get time for loading contents need to import time module
import time
# For infinite scrolling with help of page down key
from selenium.webdriver.common.keys import Keys


# function to perform facebook automation
def open_fb():
    # Creating an object to access web driver functionalities
    options = webdriver.ChromeOptions()
    # Inorder to compatible selenium with chrome browser old versions
    options.add_experimental_option("detach", True)
    # to disable browser popups and notifications
    options.add_argument("--disable-notifications")
    # importing Chromedriver installation path
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\selenium\chromedriver.exe')
    # to maximize window to full size
    driver.maximize_window()
    # getting url for facebook authentication
    driver.get("https://www.facebook.com/login/")
    # getting username field using xpath and filling required credentials
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys('***********')
    # getting password field using xpath and filling required credentials
    driver.find_element(By.XPATH, "//*[@id='pass']").send_keys('*********')
    # getting login button using name and executed click action
    driver.find_element(By.NAME, "login").click()
    # delaying process while browser loads full contents
    time.sleep(3)
    # fetching body by using classname
    element = driver.find_element(By.CLASS_NAME, '_a3wf system-fonts--body roboto')
    # for infinity scrolling
    while True:
        # page down key action to scroll down
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(3.5)

# function to perform instagram automation
def open_insta():
    # Creating an object to access web driver functionalities
    options = webdriver.ChromeOptions()
    # Inorder to compatible selenium with chrome browser old versions
    options.add_experimental_option("detach", True)
    # to disable browser popups and notifications
    options.add_argument("--disable-notifications")
    # importing Chromedriver installation path
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\selenium\chromedriver.exe')
    # to maximize window to full size
    driver.maximize_window()
    # getting url for instagram authentication
    driver.get("https://www.instagram.com/accounts/login/")
    # delaying process while browser loads full contents
    time.sleep(10)
    # getting username field using name and filling required credentials
    driver.find_element(By.NAME, "username").send_keys('************')
    # getting password field using css_selector and filling required credentials
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('********')
    # getting login button using xpath and executes click action
    driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
    time.sleep(8)
    # driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(10)
    # fetching body by using xpath
    element = driver.find_element(By.XPATH, "/html/body")
    while True:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(3.5)

# Initializing object for speech_recognition
recorder = sr.Recognizer()
# enabling microphone to listen
with sr.Microphone() as source:
    # prompting user to select Insta/ fb
      print('Which one do you prefer(Instagram/Facebook)? :')
    # taking audio input and store it in audio variable
      audio = recorder.listen(source)
    # if it's successsful user will get this notification
      print('voice captured successfully')
    # process the text in standard english format
      text = recorder.recognize_google(audio,language='en-IN')
      print(text)
    # if fb contains in audio , will call open_fb function
      if 'open' in text.lower() and 'facebook' in text.lower():
          open_fb()
    # if insta contains in audio , will call open_insta function
      elif 'open' in text.lower() and 'instagram' in text.lower() or 'insta' in text.lower():
          open_insta()
    # if audio contains other than insta / fb it will prompt this message
      else:
          print('Please select either from Facebook or Instagram!')


