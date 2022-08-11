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



def open_fb():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\selenium\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.facebook.com/login/")
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys('firozkhan6541@gmail.com')
    driver.find_element(By.XPATH, "//*[@id='pass']").send_keys('Firoz@123')
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, '_a3wf system-fonts--body roboto')
    while True:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(3.5)

def open_insta():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\selenium\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.instagram.com/accounts/login/")
    k=driver.find_element(By.CLASS_NAME, "_2hvTZ pexuQ zyHYP").send_keys('firozkhan6541@gmail.com')
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('Firoz@123')
    driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    while True:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(3.5)


recorder = sr.Recognizer()
with sr.Microphone() as source:
      print('Which one do you prefer(Instagram/Facebook)? :')
      audio = recorder.listen(source)
      print('voice captured successfully')
      text = recorder.recognize_google(audio,language='en-IN')
      print(text)
      if 'open' in text.lower() and 'facebook' in text.lower():
          open_fb()
      elif 'open' in text.lower() and 'instagram' in text.lower() or 'insta' in text.lower():
          open_insta()
      else:
          print('Please select either from Facebook or Instagram!')


