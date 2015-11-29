import os
import random


def average(elements): 
	total = 0.0
	for number in elements: 
		total += number
	return (total / len(elements))

def variance(elements): 
	diffs = []
	av = average(elements)
	for number in elements: 
		diffs.append( (number - av) * (number - av) )
	sumDiffs = 0.0 
	for diff in diffs: 
		sumDiffs += diff
	return (sumDiffs / len(elements))	

def computeNewMeanVariance(listsOfSamples): 
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
		newVar = variance(pointsList)
		return (newMean, newVar)

	    
def genList(numberNormals, mu, sigma):
    output = [] 
    for i in xrange(numberNormals): 
	output.append(random.gauss(mu, sigma))
    return output

def listify(stringList): 
	outputList = []
	stringList = stringList.replace("[", "")
	stringList = stringList.replace("]", "") 
	for element in stringList.split(","):
		outputList.append(float(element))
	return outputList

def produceGraph():
    main()
    removeLines()
    processing()
    processing2()
    finalProcessing()
    
def main():
    words = open("words.txt", "r")
    for line in words:
        word = line.strip()
        os.system(r"/WordNet/2.1/bin/wn.exe " + word + " -synsv >> output.txt")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def removeLines():
    doc = open("output.txt", "r")
    output = open("output2.txt", "w") 
    for line in doc:
        if len(line.strip()) != 0:
            output.write(line)

def processing():
    doc = open("output2.txt", "r")
    output = open("output3.txt", "w")
    for line in doc:
        written = line
        getRid = False
        if "Synonyms/Hypernyms" in written:
            getRid = True
        if "=>" in written:
            written = written.replace("=>"," ")
        if "Sense" in written:
            written = written.replace("Sense", " ")
        if is_number(written.strip()):
            getRid = True
        if " senses of " in written:
            a, b = written.split(" senses of ", 1)
            written = b.strip() + ":"
        if " sense of " in written:
            a, b = written.split(" sense of ", 1)
            written = b.strip() + ":"
        if "Also See->" in written:
            getRid = True
        if getRid == False:
            output.write(written)

def processing2():
    doc = open("output3.txt", "r")
    output = open("output4.txt", "w")
    entry = ""
    for line in doc:
        written = line
        getRid = False
        if ":" in written:
            if len(entry) != 0:
                entry = entry.replace(":", "\t")
                output.write(entry + "\n")
            entry = written.strip()
        if ":" not in written:
            entry = entry + "," + written.strip()

def finalProcessing():
    doc = open("output4.txt", "r")
    output = open("finalOutput.txt", "w")
    entry = ""
    for line in doc:
        written = line
        a, b = written.split('\t', 1)
        c = b.replace(a.strip() + ',', "")
        output.write(a + '\t' + c)

def finalTesting():
    doc = open("finalOutput.txt", "r")
    for line in doc: 
	line = line.strip()
	word, synonyms = line.split("\t", 1)
	word = word.strip()
	for synonym in synonyms.split(","):
		synonym = synonym.strip()
		if len(synonym) > 0: 
			print word + ' \t ' + synonym

main()
removeLines()
processing()
processing2()
finalProcessing()
