from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time
import json

class pars_link():
    def __init__(self, url) :
        self.filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
        self.url = url
    
    def pars_element(self):
            driver = webdriver.Chrome(self.filename)
            driver.get(url)
            time.sleep(5)
            parent  =  driver.find_element(By.CLASS_NAME,  'Constructor-PartList')
            childs_one = parent.find_elements(By.CLASS_NAME, 'ConstructorForm-Row')
            return childs_one

    def father_link(self, childs_one):
        for element, item in zip(childs_one, items[0]):
            link_task = 'Тестовая часть'
            link_task2 = 'Развёрнутая часть'
            link_task3 = 'Задания, не входящие в ЕГЭ этого года'
            pars_link = [
                        {
                        item:[
                            {link_task: {}}, 
                            {link_task2:{}},
                            {link_task3:{}}
                            ]
                        }
                        ]
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
            if link_task == father_name_link:
                update = link_task
                numb = 0
                continue
            elif link_task2 == father_name_link:
                update = link_task2
                numb = 1
                continue
            elif link_task3 == father_name_link:
                update = link_task2
                numb = 2
                continue
            pars_link[0][item][numb][update].update({father_name_link:{}})
            info_child_name_link = element.find_elements(
                                                        By.CLASS_NAME, 
                                                        'Link_wrap.ConstructorForm-TopicName.Label'
                                                        )
            return [info_child_name_link, pars_link, father_name_link, update, numb]
    
    def pars_links(self):
        childs_one = pl.pars_element()
        father_link = pl.father_link(childs_one)
        pars_link = father_link[1]
        update = father_link[3]
        numb = father_link[4]
        father_name_link = father_link[2]
        info_child_name_link = father_link[0]
        for child_name_link in info_child_name_link:
                name = ((child_name_link.get_attribute('outerText')).split('\xa0'))[0]
                link = child_name_link.find_elements(By.TAG_NAME, 'a')
                if len(link) != 0 and name != '':
                    link = link[0].get_attribute('href')
                    pars_link[numb][update][father_name_link].update({name: link})
        return pars_link
with open('father_link.json', encoding="utf8") as fl:
                items = json.load(fl)
                keys = items[0].keys()
for key in keys:
      url = items[0].get(key)
      pl = pars_link(url)
      answer = pl.pars_links()
print(answer[0])

            