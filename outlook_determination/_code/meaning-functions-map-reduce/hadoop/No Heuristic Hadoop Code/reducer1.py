#!/usr/bin/env python

import sys

graph = {}
graph['D3@DL1NK'] = []
initialMean = 0.0
initialVariance = 0.05
initialMeanNeg = -.8
initialVarianceNeg = .1
initialMeanPos = .8
initialVariancePos = .1

for line in sys.stdin:
	line = line.strip()
	title, link = line.split('\t', 1)
	newTitle = title.strip()	
	newLink = link.strip()
	if graph.has_key(newTitle):
		if newLink not in graph[newTitle]: 
			graph[newTitle].append(newLink)
	else: 
		graph[newTitle] = [newLink,] 
	
for (title, links) in graph.iteritems(): 
	if "^" in title:
		print title + ' || ' + str(initialMeanPos) + ' ||' + str(initialVariancePos) + ' ||',	  	
	elif "*" in title:
		print title + ' || ' + str(initialMeanNeg) + ' ||' + str(initialVarianceNeg) + ' ||',	  
	else: 
		print title + ' || ' + str(initialMean) + ' ||' + str(initialVariance) + ' ||',	  	
	numRealLinks = 0
	for link in links: 
		if ((link in graph) & (link != 'D3@DL1NK')):
			print link + ' :',
			numRealLinks += 1
	print '|| ' + str(numRealLinks) 
