#!C:\Python34\python.exe
# -*- coding: utf-8 -*-

class MainSec:
	def __init__(self):
		pass

	@staticmethod
	def esc_xss(word):
		word = word.replace('&', '&amp;')
		word = word.replace('<', '&lt;')
		word = word.replace('>', '&gt;')
		word = word.replace('\"', '&quot;')
		word = word.replace('\'', '&#39;')
		return word		
