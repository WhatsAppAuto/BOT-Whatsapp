#!VENV/bin/python3
# -*- coding: UTF-8 -*-


from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager
import kivy
kivy.require('1.11.1')

class Gerenciamento(ScreenManager):
	pass

class whatsbot(App):
	def build(self):
		return Gerenciamento()


if __name__ == "__main__":
	whatsbot().run()
