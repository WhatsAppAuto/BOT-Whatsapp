#!VENV/bin/python3
# -*- coding: UTF-8 -*-

import platform
from os import getcwd
from time import sleep
from pyautogui import alert
import re

from selenium import webdriver


from pyautogui import locateCenterOnScreen, click, locateOnScreen, center, typewrite, press

class BOT:
        dir_path = getcwd()

        def __init__(self):

                self.nomeDriver = self.dir_path+self.driver()

        def driver(self):

                if platform.system() == "Linux":
                        return "/drivers/Chromelinux64/chromedriver"

                elif platform.system() == "Windows":
                        return "\\drivers\\Chromewin32\\chromedriver.exe"

                else:
                        print("Sistema operacional não indetificado!")

        def inicia(self):
                self.options = webdriver.ChromeOptions()
                self.options.add_argument(r"user-data-dir="+self.dir_path+"/profile/wpp")
                self.driver = webdriver.Chrome(self.nomeDriver, chrome_options=self.options)
                self.driver.get('https://web.whatsapp.com/')
                self.driver.implicitly_wait(15)


        def procurarContato(self, nome_contato):

                try:
                        self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_2zCfw')
                        self.caixa_de_pesquisa.send_keys(nome_contato)
                        sleep(3)

                        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
                        self.contato.click()
                        sleep(2)

                except Exception as erro: alert(f'Erro em procurar Contato: {erro}')

        def mensagem(self, frase):

                try:
                        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3u328')
                        self.caixa_de_mensagem.send_keys(frase)
                        sleep(1)

                        self.botao_enviar = self.driver.find_element_by_class_name('_3M-N-')
                        self.botao_enviar.click()
                        sleep(2)
                        
                except Exception as erro:
                        alert(f'Erro em enviar mensagem: {erro}')

                

        def enviarImage(self, imagem):

                try:
                        x,y = locateCenterOnScreen(imagem)
                        click(x,y)
                        sleep(2)
                        click(x,y+80)
                        sleep(1)
                
                        typewrite(imagem)
                        sleep(1)
                        press('enter')
                        sleep(3)
                        press('enter')

                except:pass

                
                
