#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
import cgi, sys, io
from system.main_sys import MainSys
from system.main_sec import MainSec
from system.control.con_admin import ConAdmin

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html\n')
print('<!doctype html>\n<body>')

s = MainSys('name', 'mail', 'message')
s.set_con('localhost', 'root', 'mirohitogagominoyouda', 'keiziban2', 'utf8')

def show():
	cnt = 0
	for wd in iter(s.read_db('select id, name, time, mail, message from keiziban2.usershow1')):
		for inwd in wd:
			if cnt == 0:
				print('<p><b>', inwd, '.')
			elif cnt == 1:
				print(MainSec.esc_xss(inwd))
			elif cnt == 3:
				print('<p><b>Mail:', MainSec.esc_xss(inwd), '</b></p>')
			elif cnt == 4:
				inwd = MainSec.esc_xss(inwd)
				if '\n' in inwd:
					inwd = inwd.replace('\n', '<br>')
				print('<p>', inwd, '</p>')
			else:
				print(inwd, '</b></p>')

			cnt += 1
		cnt = 0
		print('<hr>')

def link_site(n):
	if 'http://' in n:
		return '<a href="{}">{}</a>'.format(n, n)


if s.Name != '' and s.Mail != '' and s.Message != '':
	s.write_db('insert into usershow1(name, mail, message) values (%s, %s, %s)', s.Name, s.Mail, s.Message)
	show()
else:
	show()

s.close_db()
print('</body>\n</html>')