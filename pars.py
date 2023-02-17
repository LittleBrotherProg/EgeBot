from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time
import json

class pars_link():

    def __init__(self, url) :
        self.filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
        self.url = url
    
    def pars_link_task(self):
        driver = webdriver.Chrome(self.filename)
        link_task = 'link task'
        link_task2 = 'links to tasks not included in this year'
        pars_link = [
                    {link_task: {}}, 
                    {link_task2:{}}
                    ]
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
            if i <= 26:
                update = link_task
                numb = 0
            else:
                update = link_task2
                numb = 1
            pars_link[numb][update].update({father_name_link:{}})
            info_child_name_link = element.find_elements(
                                                        By.CLASS_NAME, 
                                                        'Link_wrap.ConstructorForm-TopicName.Label'
                                                        )
            for child_name_link in info_child_name_link:
                name = ((child_name_link.get_attribute('outerText')).split('\xa0'))[0]
                link = child_name_link.find_elements(By.TAG_NAME, 'a')
                if len(link) != 0 and name != '':
                    link = link[0].get_attribute('href')
                    pars_link[numb][update][father_name_link].update({name: link})
        return pars_link

# u = pars_link('https://inf-ege.sdamgia.ru/')
# answer = u.pars_link_task()
# print(answer[0])

            