from mrjob.job import MRJob
import math
import random

numberSamples = 50
k = .5

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

def genList(numberNormals, mu, sigma):
	output = [] 
	for i in xrange(numberNormals): 
		output.append(random.gauss(mu, sigma))
	return output

# define new job by creating derived class
class pageRank(MRJob):

    # we need to keep the same signature as the __init__ function
    # we are overriding
    def __init__(self, *args, **kwargs):
	# this calls the MRJob __init__ function
        super(pageRank, self).__init__(*args, **kwargs)
        # create a defaultdict for each map task (default to int 0)
        self.graph = dict()
	self.pageRanks = dict()
    
    def mapper(self, key, value):
        # this does nothing.  it's required however so that the
        # compiler recognizes this as a "generator"
	value = value.replace('"', '')
	a, rest = value.split('\t', 1)
	b, c, d, e = rest.split('|', 3)
	for word in b.split(','): 
		if len(word.strip()) > 0: 
			yield a.strip(), word.strip()
			yield word.strip(), str(genList(numberSamples, float(c), float(d)))   
			yield a.strip(), c + ', ' + d + ', $'
            
#    def mapper_final(self):
#        # iterate over entries deposited by mapper and sum them
#	yield 0, (self.inside, self.total)
    
    def reducer(self, key, values):
	graphCheck = dict()
	graph = "" 
	wordCount = 0
	allSamplesList = []
	oldMean = 0
	oldVariance = 0
	newMean = 0
	newVariance = 0
	for value in values: 
		if '[' in value:
			allSamplesList.append(listify(value))
		elif '$' in value:
			oldMean, oldVariance, repSymbol = value.split(',', 2)
		elif value.strip() not in graphCheck: 
			graph += value.strip() + ', ' 
			wordCount += 1
	if '*' in key:
		newMean, newVariance = 1.0, .1
	elif '^' in key:
		newMean, newVariance = -1.0, .1
	else:
		newMean, newVariance = computeNewMeanVariance(float(oldMean), float(oldVariance), allSamplesList)
	yield key, graph + '|' + str(newMean) + '|'  + str(newVariance) + '|' + str(wordCount)

if __name__ == '__main__':
    pageRank.run()
