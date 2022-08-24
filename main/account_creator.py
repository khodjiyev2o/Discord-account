from lib2to3.pgen2 import driver
import os
from pickle import TRUE
from tkinter.tix import Tree
from selenium.webdriver.common.keys import Keys
from re import L, S
from sre_constants import SUCCESS 
from selenium import webdriver
import os
import main.constants as const
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException
import time 
import random





class Creator(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER_PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super(Creator, self).__init__(options=options)
        self.implicitly_wait(15)
        self.termsize = os.get_terminal_size()[0]
        self.left = ' '*int(self.termsize/4)
        self.token = None
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print("Exiting...")
   


    def write(self,*args, **kwargs):
        print(self.left, *args, **kwargs)

    def ask(self,prompt):
        self.write(prompt, end='')
        return input()

    def land_first_page(self):
        self.get(const.BASE_URL)

    ## account  creation    
    def registration(self,email,username):
        month = random.choice(['январь', 'февраль', 'март', 'апрель', 'май',
                                'июнь', 'июль','август','сентябр', 'октябрь', 'ноябрь', 'декабрь'])
        day = str(random.randint(1, 28))
        year = str(random.randint(1980, 2003))
        elems = self.find_elements_by_tag_name('input')
        keys = (email, username, "Samandar2021!",day, month+'\ue004', year)
    
        for text, elem in zip(keys, elems):            
            elem.send_keys(text)
            time.sleep(0.05)

        try:
            self.find_element_by_css_selector(
                'input[type="checkbox"]').click()
        except:
            pass
        self.find_elements_by_tag_name('button')[0].click()

        # while driver.find_element_by_xpath("// a[contains(text(),\'The resource is  being rate limited.')]"):
        #     self.ask(
        #         'You are being rate limited. Press enter when you\'d like to continue. . .')
        #     self.find_elements_by_tag_name('button')[0].click()

        try:
            WebDriverWait(self, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
            self.ask('Is there a captcha? Press enter once you\'ve completed it.')
        except TimeoutException:
            pass
    
    ##getting token 
    def getting_token(self):
            try:
                WebDriverWait(self, 10).until(
                    lambda self: self.current_url != 'https://discord.com/register')

                token = self.execute_script(
                    'location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"')
                use = True
                self.token = token 
                print("Аккаунт успешно был  создан : ")
                print("Ваш токен : ",token)

            except TimeoutException:
                pass



    ## login user with his token  when he already has an account in Discord
    # def login_with_token(self):
    #     self.get('https://discord.com/login')
    #     self.execute_script('window.t = "' + self.token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
