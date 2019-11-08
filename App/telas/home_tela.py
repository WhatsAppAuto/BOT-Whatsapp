#!VENV/bin/python3
# -*- coding: UTF-8 -*-

from kivy.uix.screenmanager import Screen
from pyautogui import alert
from threading import Thread
from bot import BOT
import platform
from kivy.clock import Clock
from time import sleep
import os
import json


class Home(Screen):
        def on_pre_enter(self):

                def carrega(t):

                        if os.path.exists('dados.json'):
                                self.contatos = []

                                with open('dados.json', 'r') as arquivo:

                                        self.infors = json.load(arquivo)
                                        arquivo.close()

                                for text in self.infors['contatos']:

                                        if text != "":
                                                self.ids.contatos.text += text
                                                self.ids.img.text = self.infors["image"]
                                                self.ids.mensagem.text = self.infors['mensagem']



                        if os.path.exists('profile') == False:
                                self.ids.perfilWb.text = "Seus dados serão salvos\n depois que scanear o codigo QR"

                Clock.schedule_once(carrega, 1)
 
        def Enviar(self):
                texto = """
                Não use o computador, durante a execução do programa!
                """

                alert(title="Mensagem", text=texto)
                self.enviando = Thread(target=self.TH)
                self.enviando.start()

        def TH(self):

                self.contatos = self.ids.contatos.text.split(',')
                self.mensagem = self.ids.mensagem.text

                if self.contatos != [] and self.mensagem != '':
                        self.bot = BOT()
                        self.bot.inicia()

                        alert(title="Esperando WhatsappWeb Carregar!", text='Quando o Whatsapp web estiver carregado clique em OK')

                        for contato in self.contatos:
                                if contato[0] != "" and contato[0] != " ":
                                        self.bot.procurarContato(contato)

                                else:
                                        contato = contato[1::]
                                        self.bot.procurarContato(contato)
                                        
                                if self.ids.img.text != "":
                                        self.bot.enviarImage(self.ids.img.text)
                                        sleep(2)
                                        
                                self.bot.mensagem(self.mensagem)
                                sleep(1)

                        alert(title="Mensagem", text="Terminado!")
                
        def apagarPerf(self):
                if os.path.exists('profile'):

                        if platform.system() == "Linux":
                                os.system('rm -r profile')

                        elif platform.system() == "Windows":
                                os.system('rd /s /q profile')

                        else:
                                print()
                                


        def salvarDados(self):
                infors = {
                        "image": self.ids.img.text,
                        "contatos": self.ids.contatos.text,
                        "mensagem": self.ids.mensagem.text
                        }

                with open('dados.json', 'w') as arquivo:
                        json.dump(infors, arquivo)



