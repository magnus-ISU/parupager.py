#!/bin/python3

import os
import sys
from colorama import Fore, Back, Style
from click import echo_via_pager

packages = []
max_name = 0

perfect_match = []

pkg = []
for line in sys.stdin:
	if line[0] != " ":
		if len(pkg) != 0:
			packages.append(pkg)
			pkg = []
		line = line.strip()
		length = len(line.split('/')[1])
		if length > max_name:
			max_name = length
	else:
		line = line.strip()
	pkg.append(line)

if len(pkg) != 0:
	packages.append(pkg)

SEPERATOR = " | "
cols, rows = os.get_terminal_size()
max_desc = cols - max_name - len(SEPERATOR) - 2
color = Fore.CYAN

if max_desc < max_name:
	print('BADNESS 1000')

current_repo = ""
for package in packages:
	reposplit = package[0].split('/')
	if reposplit[0] != current_repo:
		current_repo = reposplit[0]
		echo_via_pager(Fore.YELLOW + ''.ljust(cols, '-') + f'\n    {current_repo}\n' + ''.ljust(cols, '-'))
	package[0] = reposplit[1]

	if color == Style.RESET_ALL:
		color = Fore.CYAN
	else:
		color = Style.RESET_ALL
	print(color, end=' ')

	print(package[0].ljust(max_name), end='')
	for packagedesc in package[1:]:
		first_desc = True
		while True:
			if first_desc:
				first_desc = False
				print(Style.RESET_ALL + SEPERATOR + color, end='')
			else:
				print(''.ljust(max_name), end=' ')
				print(Style.RESET_ALL + SEPERATOR + color, end='  ')
			if len(packagedesc) > max_desc:
				split_index = packagedesc[:max_desc].rfind(' ')
				if split_index == 0:
					split_index = max_desc
				print(packagedesc[:split_index])
				packagedesc = packagedesc[split_index:]
			else:
				print(packagedesc)
				break
