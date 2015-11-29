#!/usr/bin/env python

import sys

graph = {}
samples = {}
means = {}
variances = {}
k = .5
def listify(stringList): 
	outputList = []
	stringList = stringList.replace("[", "")
	stringList = stringList.replace("]", "") 
	for element in stringList.split(","):
		outputList.append(float(element))
	return outputList

def average(elements): 
	total = 0.0
	for number in elements: 
		total += number
	return (total / len(elements))

def varianceCal(elements): 
	diffs = []
	av = average(elements)
	for number in elements: 
		diffs.append( (number - av) * (number - av) )
	sumDiffs = 0.0 
	for diff in diffs: 
		sumDiffs += diff
	return (sumDiffs / len(elements))	

def computeNewMeanVariance(oldMean, oldVariance, listsOfSamples): 
	pointsList = []
	if len(listsOfSamples) == 0: 
		return (0.0, 0.0)
	else: 
		for i in xrange(len(listsOfSamples[0])):
			dataPoint = 0.0
			for j in xrange(len(listsOfSamples)): 
				dataPoint += listsOfSamples[j][i]
			pointsList.append(dataPoint / len(listsOfSamples))
		newMean = average(pointsList)
		newVar = varianceCal(pointsList)
		
		return ((k * newMean) + ((1.0 -k) * oldMean), (k * newVar) + ((1.0 -k) * oldVariance))

for line in sys.stdin:
	isPageRank = True
	
	page, content = line.split('\t', 1)
	page = page.strip()
	if (("[" in content) & ("]" in content)):
		samplesList = listify(content)
		b = samples.get(page, [])
		b.append(samplesList)
		samples[page] = b
	elif "$t@t$" in content :
		mean, variance, rando = content.split('||', 2)
		means[page] = float(mean)
		variances[page] = float(variance)
	else: 
		graph[page] = content

for (title, content) in graph.iteritems():
	newMeanVariance = (means[title], variances[title])
	if title in samples: 
		newMeanVariance = computeNewMeanVariance(means[title], variances[title], samples[title])
	if "*" in title: 
		print title + ' || ' + str(means[title]) + ' || ' + str(variances[title]) + ' || ' + content,
	elif "^" in title: 
		print title + ' || ' + str(means[title]) + ' || ' + str(variances[title]) + ' || ' + content,
	else: 
		print title + ' || ' + str(newMeanVariance[0]) + ' || ' + str(newMeanVariance[1]) + ' || ' + content,

