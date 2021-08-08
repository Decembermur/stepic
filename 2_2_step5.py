import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element=browser.find_element_by_id("input_value")
    x =x_element.text
    y = calc(x)

    Answer_Pole=browser.find_element_by_id("answer")
    Answer_Pole.send_keys(y)

    option1=browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2=browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    option3=browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    
finally:
    
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   