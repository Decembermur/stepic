import time
from selenium import webdriver
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1=browser.find_element_by_css_selector("[name='firstname']")
    option1.send_keys("Mur")
    
    option2=browser.find_element_by_css_selector("[name='lastname']")
    option2.send_keys("Mur")
    
    option3=browser.find_element_by_css_selector("[name='email']")
    option3.send_keys("Mur")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    element=browser.find_element_by_id("file")
    element.send_keys(file_path)
    option4=browser.find_element_by_css_selector("[type='submit']")
    option4.click()
    
finally:
    
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   