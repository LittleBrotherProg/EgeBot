from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time
import json

class pars_link():
    def __init__(self, academic_subject, url) :
        self.filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
        self.AS = academic_subject
        self.url = url
    
    def pars_list_task(self):
            driver = webdriver.Chrome(self.filename)
            driver.get(url)
            time.sleep(5)
            parent  =  driver.find_element(By.CLASS_NAME,  'Constructor-PartList')
            childs_one = parent.find_elements(By.CLASS_NAME, 'ConstructorForm-Row')
            return childs_one

    def creating_template(self):
            pars_link ={
                        self.AS:[
                                {'Тестовая часть': {}}, 
                                {'Развернутая часть':{}},
                                {'Задания, не входящие в ЕГЭ этого года':{}}
                                ]
                        }
                            
            return [pars_link, self.AS]

    def chek_nameFather(self, element):
        try:
                father_name_link = (element.find_elements(By.TAG_NAME, 'u')
                        )[0].get_property('innerText')
                return father_name_link
        except IndexError:
                father_name_link = (element.find_elements(By.CLASS_NAME, 'ConstructorForm-TopicDesc')
                        )[0].get_property('innerText')
                return father_name_link
                
        
            
    def father_LinkName(self):
        childs_one = pl.pars_list_task()
        pars_link, item = pl.creating_template()
        for LinkName in childs_one:
            element = LinkName.find_element(By.CLASS_NAME, 'ConstructorForm-Topic')
            time.sleep(0.5)
            element.click()
            try:
                number_father = element.find_elements(By.CLASS_NAME, 'ConstructorForm-TopicNumber')[0].get_attribute('innerText')
            except IndexError:
                 number_father = ''
            if 'Тестовая часть' == element.get_attribute('innerText'):
                    row_label = 'Тестовая часть'
                    numb = 0
                    continue
            elif 'Развернутая часть' == element.get_attribute('innerText'):
                    row_label = 'Развернутая часть'
                    numb = 1
                    continue
            elif "Задания, не\xa0входящие в\xa0ЕГЭ этого года" == element.get_attribute('innerText'):
                    row_label = "Задания, не входящие в ЕГЭ этого года"
                    numb = 2
                    continue
            else:
                    father_name_link = pl.chek_nameFather(element)
                    father_name_link = number_father + father_name_link
                    pars_link[item][numb][row_label].update({father_name_link:{}})
                    info_child_name_link = element.find_elements(
                                                        By.CLASS_NAME, 
                                                        'ConstructorForm-TopicDesc'
                                                        )
                    pl.pars_links(info_child_name_link, pars_link, item, row_label, numb, father_name_link)
            
        return  pars_link
    
    def pars_links(self, info_child_name_link, pars_link, item, row_label, numb, father_name_link):
        for child_name_link in info_child_name_link:
                name = ((child_name_link.get_attribute('outerText')).split('\xa0'))[0]
                link = child_name_link.find_elements(By.TAG_NAME, 'a')
                if len(link) != 0 and name != '':
                    link = link[0].get_attribute('href')
                    pars_link[item][numb][row_label][father_name_link].update({name: link})
                
with open('father_link.json', encoding="utf8") as fl:
                items = json.load(fl)
                keys = items[0].keys()
inf =[]
for key in keys:
      url = items[0].get(key)
      pl = pars_link(key, url)
      answer = pl.father_LinkName()
      inf.append(answer)
with open('all_task.json', 'w', encoding='utf-8') as all_task:
       json.dump(
                inf,
                all_task,
                sort_keys=False,
                indent=4,
                ensure_ascii=False,
                separators=(',', ': ')
                )

            