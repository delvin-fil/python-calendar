#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import datetime,time, calendar, re, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8') 
days = {0: u"${alignc}Понедельник", 1: u"${alignc}Вторник", 2: u"${alignc}Среда", 3: u"${alignc}Четверг", 4: u"${alignc}Пятница", 5: u"${color FF0000}${alignc}Суббота", 6: u"${color FF0000}${alignc}Воскресенье"}
ds = days[datetime.date.today().weekday()]
localtime = time.localtime(time.time())
calendar.setfirstweekday(calendar.MONDAY)
cal = calendar.month(localtime[0], localtime[1])
parts = cal.split('\n')

cal = '${font Ubuntu:size=10}\n' + ds + '${color 00CCFF}${voffset -3}\n' +'${alignc 10}${font Monospace:size=13:bold}' + '\n${offset 22}${voffset -3}${font Monospace:size=10:bold}'.join(parts)

b = '(?<=)'
a = '(?<= )'
if localtime[2] > 9:
	c = b
else:
	c = a 
regex = c + '%s(?= )|(?<=\n )%s(?= )|(?<= )%s(?=\n)' % (localtime[2], localtime[2], localtime[2]) 
replace = '${color FF0000}${voffset 2}${offset -2}${font a_FuturaRoundTitulCm:size=11:bold}%s${color ffff00}${font Monospace:size=10:bold}${voffset -2}${offset -2}' % localtime[2]
newCal = re.sub(regex, replace, cal)
rewek = re.sub('Сб Вс', '${color FF0000}Сб Вс${color 666666}', newCal)
rewek = re.sub('Пн Вт Ср Чт Пт', '${color FFFFFF}Пн Вт Ср Чт Пт${color 666666}', rewek)

print (rewek)
