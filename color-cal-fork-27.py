#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
import datetime, time, calendar, re, locale
from colorama import Fore, Back, Style
locale.setlocale(locale.LC_ALL, '')
#------------------------------------

localtime = time.localtime(time.time())
calendar.setfirstweekday(calendar.MONDAY)
cal = calendar.month(localtime[0],localtime[1])
parts = cal.split('\n')
cal = Fore.GREEN + '\n'.join(parts)+ Fore.WHITE
regex = '(?<= )%s(?= )|(?<=\n)%s(?= )|(?<= )%s(?=\n)' % (localtime[2], localtime[2], localtime[2])
replace = Fore.RED + '%s'  %   localtime[2]
newCal = re.sub(regex, replace + Fore.WHITE, cal)
rewek = re.sub('С В', Fore.RED + 'С  В' + Fore.CYAN, newCal)
rewek = re.sub('П В С Ч П', Fore.YELLOW + ' П  В  С  Ч  П ', rewek)

#print (newCal)
print (rewek)

