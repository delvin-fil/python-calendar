#!/usr/bin/env python
# Комментировать не стал, думаю и так все понятно, если хоть
# одну книгу по питону открывал :)
# Но если надо...
import datetime,time, calendar, re, locale

locale.setlocale(locale.LC_ALL, '') 
days = {0: u"Понедельник", 1: u"Вторник", 2: u"Среда", 3: u"Четверг", 4: u"Пятница", 5: u"${color FF0000}${alignc}Суббота", 6: u"${color FF0000}${alignc}Воскресенье"}
ds = days[datetime.date.today().weekday()]

localtime = time.localtime(time.time())
calendar.setfirstweekday(calendar.MONDAY)
cal = calendar.month(localtime[0], localtime[1])
parts = cal.split('\n')
# найти куда пнуть ${color 666666} 
cal = '${font Ubuntu:size=10}\n' + ds + '${color 00CCFF}${voffset -2}\n' +'${font Monospace:size=11:bold}${offset -18}' + '\n${voffset -2}${font Monospace:size=8:bold}'.join(parts)

b = '(?<=)'
a = '(?<= )'
if localtime[2] > 9:
	c = b
else:
	c = a 
regex = c + '%s(?= )|(?<=\n )%s(?= )|(?<= )%s(?=\n)' % (localtime[2], localtime[2], localtime[2]) 
replace = '${color FF0000}%s${color ffff00}' % localtime[2]
newCal = re.sub(regex, replace, cal)
rewek = re.sub('Сб Вс', '${color FF0000}Сб Вс${color 666666}', newCal)
rewek = re.sub('Пн Вт Ср Чт Пт', '${color FFFFFF}Пн Вт Ср Чт Пт${color 666666}', rewek)
#print (newCal)
print (rewek)
#----------------------------------------------
