#-*- coding: utf-8 -*-
f= open('20140226(2013).txt','r')
lines = f.readlines()
f.close()

for line in lines:
	if 'AHOTHER' in line:
		lines.remove(line)

print len(lines)