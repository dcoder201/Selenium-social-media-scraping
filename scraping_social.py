import speech_recognition as sr
import pyaudio
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\selenium\chromedriver.exe')
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH, "//*[@id='email']").send_keys('************')
driver.find_element(By.XPATH, "//*[@id='pass']").send_keys('******')
driver.find_element(By.NAME, "login").click()

total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

# recorder = sr.Recognizer()
# with sr.Microphone() as source:
#     print('Say Something:')
#     audio = recorder.listen(source)
#     print('voice processed completely...')
# text = recorder.recognize_google(audio,language='ml-IN')
# print(text)