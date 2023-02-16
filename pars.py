from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time
import json
filename = DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
driver = webdriver.Chrome(filename)
url = 'https://inf-ege.sdamgia.ru/'
urls_child= []
driver.get('https://inf-ege.sdamgia.ru/')
time.sleep(5)
parent  =  driver.find_element(By.CLASS_NAME,  'Constructor-PartList')
childs_one = parent.find_elements(By.CLASS_NAME, 'ConstructorForm-Row')
del childs_one[0]
for i, element in enumerate(childs_one):
    element = element.find_elements(By.CLASS_NAME, 'ConstructorForm-Topic')[0]
    time.sleep(0.5)
    element.click()
    father_name_link = (element.find_elements(By.TAG_NAME, 'u')
                )[0].get_property('outerText')
    info_child_name_link = element.find_elements(
                                            By.CLASS_NAME, 
                                            'Link_wrap.ConstructorForm-TopicName.Label'
                                            )
    for child_name_link in info_child_name_link:
        name = child_name_link.get_attribute('outerText')
        link = child_name_link.find_elements(By.TAG_NAME, 'a')
        if len(link) != 0:
            link = link[0].get_attribute('href')
    time.sleep(0.5)
print(urls_child)