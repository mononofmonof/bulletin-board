#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
import cgi, sys, io
from system.main_sys import MainSys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html\n')
print('<!doctype html>\n<body>')

s = MainSys('name', 'mail', 'message')
s.set_con('localhost', 'root', 'pass', 'table', 'utf8')

def show():
	cnt = 0
	for wd in iter(s.read_db('select id, name, time, mail, message from keiziban2.usershow1')):
		for inwd in wd:
			if cnt == 0:
				print('<p><b>', inwd, '.')
			elif cnt == 1:
				print(inwd)
			elif cnt == 3:
				print('<p><b>Mail:', inwd, '</b></p>')
			elif cnt == 4:
				if '\n' in inwd:
					inwd = inwd.replace('\n', '<br>')
				print('<p>', inwd, '</p>')
			else:
				print(inwd, '</b></p>')

			cnt += 1
		print('<hr>')


if s.Name != '' and s.Mail != '' and s.Message != '':
	s.write_db('insert into usershow1(name, mail, message) values (%s, %s, %s)', s.Name, s.Mail, s.Message)
	show()
else:
	show()

s.close_db()

print('</body>\n</html>')