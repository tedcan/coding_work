#!/usr/bin/env python

import sys

for line in sys.stdin: 
	pageTitle, mean, variance, links, numberLinks = line.split('||', 4)

	pageTitle = pageTitle.strip()
	value = float(mean)
	print pageTitle + ' \t ' + str(value) + " || " + variance



