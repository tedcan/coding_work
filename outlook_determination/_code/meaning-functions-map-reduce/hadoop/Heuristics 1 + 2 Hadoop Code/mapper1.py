#!/usr/bin/env python

import sys

for line in sys.stdin:

	links = []

	line = line.strip()
	
	word, content = line.split("\t", 1)
	synonyms, prior = line.split("||", 1)
	prior = float(prior)
	print word + ' \t ' + str(prior) + " pr10r "
	word = word.strip()
	for synonym in synonyms.split(","):
		synonym = synonym.strip()
		if len(synonym) > 0: 
			print synonym + ' \t ' + word
