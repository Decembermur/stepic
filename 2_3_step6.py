import time
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1=browser.find_element_by_css_selector("[type='submit']")
    option1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    option2=browser.find_element_by_css_selector("#input_value")
    x=option2.text
    y=calc(x)
    
    Answer_Pole=browser.find_element_by_id("answer")
    Answer_Pole.send_keys(y)
    
    option3=browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    
    
    
finally:
    
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   