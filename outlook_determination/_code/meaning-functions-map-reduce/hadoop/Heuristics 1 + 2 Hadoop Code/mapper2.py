#!/usr/bin/env python

import sys
import random

numberSamples = 50


def genList(numberNormals, mu, sigma):
	output = [] 
	for i in xrange(numberNormals): 
		output.append(random.gauss(mu, sigma))
	return output

for line in sys.stdin: 
	if len(line.strip()) > 0: 
		pageTitle, mean, variance, links, numberLinks = line.split('||', 4)

		pageTitle = pageTitle.strip()
		numberLinks = int(numberLinks.strip())
		mean = float(mean)
		variance = float(variance)
		print pageTitle + ' \t ' + links + ' || ' + str(numberLinks)
		print pageTitle + ' \t ' + str(mean) + ' || ' + str(variance) + ' || ' + "$t@t$"

		if numberLinks == 0: 
			# If it's a dead-end page, and there are no links
			print 'D3@DL1NK' + ' \t ' + str(genList(numberSamples, 0, 0))
		else: 
			for link in links.split(':'):	
				link = link.strip() 
				if len(link) > 0: 
					print link + ' \t ' + str(genList(numberSamples, mean, variance)) 




