#!/usr/bin/env python

import sys

top10 = []

for line in sys.stdin:
	pageTitle, pageRank = line.split('\t', 1) 
	pageTitle = pageTitle.strip()
	pageRank = pageRank.strip()
	top10.append((pageTitle, pageRank))

for element in top10:
	print str(element[0]) + ' \t ' + element[1]
