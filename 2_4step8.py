import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    
    optionB=browser.find_element_by_css_selector("#book")
    element=WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID,"price"),"100")
    )
    optionB.click()
    time.sleep(1)
    
    
    option2=browser.find_element_by_css_selector("#input_value")
    x=option2.text
    y=calc(x)
    
    Answer_Pole=browser.find_element_by_id("answer")
    Answer_Pole.send_keys(y)
    
    option3=browser.find_element_by_css_selector("#solve")
    option3.click()
    
    
    
finally:
    
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   