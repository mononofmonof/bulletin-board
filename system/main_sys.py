#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
import pymysql
import cgi, sys, io

class MainSys:

	f = cgi.FieldStorage()

	def __init__(self, *rec: str):
		self._connection = None
		self._cursor = None
		self._name = MainSys.f.getfirst(rec[0], '')
		self._mail = MainSys.f.getfirst(rec[1], '')
		self._message = MainSys.f.getfirst(rec[2], '')

	@property
	def Name(self) -> str:
		return self._name
	
	@property
	def Mail(self) -> str:
		return self._mail
	
	@property
	def Message(self) -> str:
		return self._message
	

	def set_con(self, *con: str):
		self._connection = pymysql.connect(
						host=con[0],
						user=con[1], 
						password=con[2], 
						db=con[3], 
						charset=con[4]
					)

		self._cursor = self._connection.cursor()


	def read_db(self, sql: str):
		self._cursor.execute(sql)
		for _ in self._cursor.fetchall():
			yield _


	def write_db(self, sql: str, *rec: str):
		self._cursor.execute(sql, (rec[0], rec[1], rec[2]))
		self._connection.commit()


	def close_db(self):
		self._cursor.close()
		self._connection.close()