#!/usr/bin/env python

import sys

for line in sys.stdin:

	links = []

	line = line.strip()
	
	word, synonyms = line.split("\t", 1)
	word = word.strip()
	for synonym in synonyms.split(","):
		synonym = synonym.strip()
		if len(synonym) > 0: 
			print synonym + ' \t ' + word
