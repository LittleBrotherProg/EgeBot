from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time
import json
filename = DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
driver = webdriver.Chrome(filename)
url = 'https://inf-ege.sdamgia.ru/'
pars_link = [{'link_task': {}}]
driver.get('https://inf-ege.sdamgia.ru/')
time.sleep(5)
parent  =  driver.find_element(By.CLASS_NAME,  'Constructor-PartList')
childs_one = parent.find_elements(By.CLASS_NAME, 'ConstructorForm-Row')
del childs_one[0]
for i, element in enumerate(childs_one):
    element = element.find_elements(By.CLASS_NAME, 'ConstructorForm-Topic')[0]
    time.sleep(0.5)
    element.click()
    try:
        father_name_link = (element.find_elements(By.TAG_NAME, 'u')
                )[0].get_property('outerText')
    except IndexError:
        father_name_link = (element.find_elements(
                                                  By.CLASS_NAME, 
                                                  'ConstructorForm-TopicDesc'
                                                  ))[0].get_attribute('innerText')
    pars_link[0]['link_task'].update({father_name_link:{}})
    info_child_name_link = element.find_elements(
                                            By.CLASS_NAME, 
                                            'Link_wrap.ConstructorForm-TopicName.Label'
                                            )
    for child_name_link in info_child_name_link:
        name = ((child_name_link.get_attribute('outerText')).split('\xa0'))[0]
        link = child_name_link.find_elements(By.TAG_NAME, 'a')
        if len(link) != 0 and name != '':
            link = link[0].get_attribute('href')
            pars_link[0]['link_task'][father_name_link].update({name: link})
    if i == 27:
        print(pars_link)
        break
    