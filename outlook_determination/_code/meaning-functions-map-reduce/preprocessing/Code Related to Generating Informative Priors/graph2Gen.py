import os
import random
import math

negList = []
posList = []
priors = {}

def main3():
    main2()
    process2()
    checkDefs()
    createNewInput()

def createNewInput():
    calculatePriors()
    graph = open("graph.txt", "r")
    finalGraph = open("finalGraph.txt", "w")
    for line in graph:
        a, b = line.split("\t", 1)
        a = a.strip()
        b = b.strip()
        if a in priors:
            line = a + "\t" + b + " || " + str(priors[a]) + "\n"
            finalGraph.write(line)
        else:
            line = a + "\t" + b + " || " + str(0.0) + "\n"
            finalGraph.write(line) 
    
    

def confidenceFunction(n):
    a = 1 - math.exp(-.4 * n)
    return a


def calculatePriors():
    global priors
    posNegCounts = open("posNegCounts.txt", "r")
    for line in posNegCounts: 
        a, b = line.split("\t")
        a = a.strip()
        if len(a) > 0:
            neg, pos = b.split(" || ")
            neg = float(neg)
            pos = float(pos)
            confidence = confidenceFunction(neg + pos)
            if (pos + neg) == 0:
                priors[a] = 0
            else:     
                prior = (( pos - neg) / ( pos + neg)) * confidence
                priors[a] = prior

def checkDefs():
    loadNegPosDicts()
    definitions = open("processedDefs.txt", "r")
    posNegCounts = open("posNegCounts.txt", "w")
    for line in definitions:
        posCount = 0
        negCount = 0
        word, defWords = line.split("\t", 1)
        for defWord in defWords.split(","):
            defWord = defWord.strip()
            defWord = defWord.lower()
            if defWord in negList:
                negCount += 1
            if defWord in posList:
                posCount += 1
        posNegCounts.write(word + "\t" + str(negCount) + " || " + str(posCount) + "\n")
    

def main2():
    words = open("graph.txt", "r")
    for line in words:
        word, stuff = line.split("\t", 1)
        word = word.strip()
        os.system(r"/WordNet/2.1/bin/wn.exe " + word + " -over >> rawDefs.txt")
        
def process2():
    definitions = open("rawDefs.txt", "r")
    processedDefinitions = open("processedDefs.txt", "w")
    titleLine = ""
    wordsInDef = ""
    for line in definitions:
        if "Overview of " in line:
            processedDefinitions.write(titleLine + "\t" + wordsInDef + "\n")
            wordsInDef = ""
            titleLine = ""
            line = line.replace("Overview of ", "")
            line = line.strip()
            wordType, word = line.split(" ", 1)
            titleLine = word

        else:
            for token in line.split(" "):
                token = token.strip(")0123456789=><(,.-;"" \t")
                token = token.strip()
                token = token.rstrip(')')
                token = token.lstrip('"')
                token = token.rstrip('"')
                if len(token) > 0: 
                    wordsInDef = wordsInDef + ", " + token

def loadNegPosDicts():
    global posList
    global negList
    negwords = open("negwords.txt", "r")
    poswords = open("poswords.txt", "r")
    for line in negwords:
        line = line.strip()
        line = line.lower()
        if len(line) > 0:
            negList.append(line)
    for line in poswords:
        line = line.strip()
        line = line.lower()
        if len(line) > 0:
            posList.append(line)
    

            
    


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
        os.system(r"WordNet/2.1/bin/wn.exe " + word + " -synsv >> output.txt")

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

#main2()
process2()
checkDefs()
createNewInput()
