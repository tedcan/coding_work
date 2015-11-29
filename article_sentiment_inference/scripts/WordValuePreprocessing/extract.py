import os
import string
import re

wordList = []
uniqueWordCount = -1
positivePriors = ['sustain', 'contribute', 'culminate', 'win', 'captivate',
                  'encourage', 'adapt', 'assure', 'grace', 'reward',
                  'master', 'expand', 'recommend', 'surge', 'arise',
                  'appreciate', 'hasten', 'score', 'preserve', 'accomplish',
                  'progress', 'succeed', 'rejoice', 'improve', 'fascinate',
                  'revolutionize', 'sustain', 'enjoy', 'rejuvenate', 'benefit']
negativePriors = ['foul', 'loathe', 'cheat', 'expire', 'hurt', 'revolt',
                  'secede', 'damage', 'threaten', 'collapse', 'idle',
                  'concede', 'decry', 'bust', 'fail', 'resign', 'pressure',
                  'downgrade', 'worsen', 'hate', 'argue', 'criticise',
                  'impoverish', 'decrease', 'beset', 'lose', 'derail',
                  'prohibit', 'choke', 'blame'] 

wordsToEliminate = ['that', 'would', 'from', 'will', 'this', 'with', 'they', 'than',
                    'have', 'into', 'about', 'make', 'which', 'them', 'their', 'what',
                    'only', 'take', 'when', 'where', 'after']

def runAll():
    runFirst()
    runSecond()
    

def runFirst():
    parseArticles()
    parsePunctuation()
    getWordList()
    getFinalFormattedProperArticles()

def runSecond():
    processing()
    processing2()
    processing3()
    finalProcessing()
    finalFinalProcessing()
    

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', data)

def parseArticles():
    w = open('OutputFiles/originalArticles.txt', 'w')
    for i in range(10000):
        path = 'InputFiles/Articles/article' + str(i) + ".htm"
        if os.path.isfile(path):
            #print "Article " + str(i) + " found"
            f = open(path, 'r')
            content = ""
            indicator = 0
            for line in f.readlines():
                if "<div class=\"content\">" in line:
                    indicator = 1
                if indicator == 1:
                    content += " " + line
                if (indicator == 1) & ("</div>" in line):
                    indicator = 0
            # Remove HTML tags and punctuation
            content = remove_html_tags(content)
            content = content.replace("\n", " ")
            if (len(content.replace(" ", "")) > 50):
                w.write(content + " \n ")
            f.close()
    w.close()

def parsePunctuation():
    w = open('IntermediateFiles/formattedArticles.txt', 'w')
    f = open('OutputFiles/originalArticles.txt', 'r')
    for line in f.readlines():
            line = line.replace("'", ' ')
            for mark in string.punctuation:
                line = line.replace(mark, ' ')
            line = line.lower()
            # Removes numbers
            line = re.sub("\d+", " ", line)
            w.write(line)
    f.close()
    w.close()


def getWordList():
    totalWordCount = 0
    wordDict = dict()
    w2 = open('IntermediateFiles/similarWords.txt', 'w')
    w = open('IntermediateFiles/wordList.txt', 'w')
    f = open('IntermediateFiles/formattedArticles.txt', 'r')
    for line in f.readlines():
        for word in line.split():
            word = word.strip()
            if (len(word) > 3) & (word.isalnum()):
                if word not in wordDict:
                    wordDict[word] = 1
                else:
                    wordDict[word] += 1
    counter = 0
    for key in wordDict:
        print counter
        counter += 1
        # Wordnet needs to be in the C:// directory.
        os.system(r"/WordNet/2.1/bin/wn.exe " + key + " -synsv >> wordNetOutputTemp.txt")
        os.system(r"/WordNet/2.1/bin/wn.exe " + key + " -synsv >> IntermediateFiles/wordNetOutput.txt")
        mappedTo = identifyFirstEntry()
        os.system("del wordNetOutputTemp.txt")
        w2.write(key.strip() + ',' + mappedTo.strip() + '\n')
        print mappedTo + ',' + key
        #if (len(mappedTo.strip()) > 0) & (len(key.strip()) > 0):
        #    diffForms[key.strip()] = mappedTo.strip()
            
                
        totalWordCount += wordDict[key]
        toWrite = key + " | " + str(wordDict[key]) + " \n "
        w.write(toWrite)
    w.close()
    f.close()
    w2.close()
    #print "Total Word Count: " + str(totalWordCount)
    #print "Total Unique Words: " + str(len(wordDict))

def getFinalFormattedProperArticles():
    diffForms = dict()
    f2 = open('IntermediateFiles/similarWords.txt', 'r')
    for line in f2.readlines():
        a, b = line.split(',', 1)
        if len(b.strip()) > 0:
            diffForms[a.strip()] = b.strip()
        
    w = open('OutputFiles/parsedArticles.txt', 'w')
    f = open('IntermediateFiles/formattedArticles.txt', 'r')
    for line in f.readlines():
        result = line
        #print line
        for word in line.split(' '):
            if word.strip() in wordsToEliminate:
                result = result.replace(' ' + word.strip() + ' ', ' ') 
            if len(word.strip()) < 4:
                result = result.replace(' ' + word.strip() + ' ', ' ')
            if (len(word.strip()) > 0) & (word.strip() in diffForms):
                result = result.replace(' ' + word.strip() + ' ', ' ' + diffForms[word.strip()] + ' ')              
                #print word.strip() + ' converted into ' + diffForms[word.strip()] 
        w.write(result)
    w.close()
    f.close()

def identifyFirstEntry():
    result = ""
    temp = open('wordNetOutputTemp.txt', 'r')
    for line in temp.readlines():
        if " senses of " in line:
            a, b = line.split(" senses of ", 1)
            result = b.strip()
        if " sense of " in line:
            a, b = line.split(" sense of ", 1)
            result = b.strip()
    temp.close()
    return result
        
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def processing():
    doc = open("IntermediateFiles/wordNetOutput.txt", "r")
    output = open("IntermediateFiles/processedWordNetOutput.txt", "w")
    for line in doc:
        if len(line.strip()) != 0:
            writtenline = line
            terminate = False
            if is_number(writtenline.strip()):
                terminate = True
            if "Also See->" in writtenline:
                terminate = True
            if "Synonyms/Hypernyms" in writtenline:
                terminate = True
            if "=>" in writtenline:
                writtenline = writtenline.replace("=>"," ")
            if "Sense" in writtenline:
                writtenline = writtenline.replace("Sense", " ")
            if " sense of " in writtenline:
                a, b = writtenline.split(" sense of ", 1)
                writtenline = b.strip() + ":"
            if " senses of " in writtenline:
                a, b = writtenline.split(" senses of ", 1)
                writtenline = b.strip() + ":"
            if terminate == False:
                output.write(writtenline)
    doc.close()
    output.close()

def processing2():
    document = open("IntermediateFiles/processedWordNetOutput.txt", "r")
    outputDocument = open("IntermediateFiles/roughGraph.txt", "w")
    constructedEntry = ""
    # Start building string consisting of the entries for one looked up word
    for line in document:
        writtenline = line
        if ":" in writtenline:
            if len(constructedEntry) > 0:
                constructedEntry = constructedEntry.replace(":", "\t")
                outputDocument.write(constructedEntry + "\n")
            constructedEntry = writtenline.strip()
        if ":" not in writtenline:
            constructedEntry = constructedEntry + "," + writtenline.strip()
    document.close()
    outputDocument.close()

def processing3():
    doc = open("IntermediateFiles/roughGraph.txt", "r")
    output = open("IntermediateFiles/trimmedGraph.txt", "w")
    entry = ""
    for line in doc:
        written = line
        a, b = written.split('\t', 1)
        c = b.replace(a.strip() + ',', "")
        output.write(a + '\t' + c)
    doc.close()
    output.close()

# Eliminate extras, add priors, add preliminary ranks
def finalProcessing():
    checkDict = dict()
    doc = open("IntermediateFiles/trimmedGraph.txt", "r")
    for line in doc:
        a, b = line.split('\t', 1)
        a = a.strip()
        if a not in checkDict:
            checkDict[a] = 1
    doc.close()
    output = open("IntermediateFiles/almostFinalGraph.txt", "w")
    doc = open("IntermediateFiles/trimmedGraph.txt", "r")
    alreadyThere = dict()
    for line in doc:
        a, b = line.split('\t', 1)
        if a.strip() not in alreadyThere:
            alreadyThere[a.strip()] = 1
            newB = ""
            wordCount = 0
            for word in b.split(','):
                word = word.strip()
                if word in checkDict:
                    wordCount += 1
                    newB += (word + ", ")

            if a.strip() in positivePriors:     
                output.write(a + '*' + '\t' + newB + '|' + '1.0' + '|' + '.1' + '|' + str(wordCount) + '\n')
            elif a.strip() in negativePriors:     
                output.write(a + '^' + '\t' + newB + '|' + '-1.0' + '|' + '.1' + '|' + str(wordCount) + '\n')
            else:
                output.write(a + '\t' + newB + '|' + '0.0' + '|' + '.1' + '|' + str(wordCount) + '\n')
    doc.close()
    output.close()
    doc = open("IntermediateFiles/almostFinalGraph.txt", "r")
    doc2 = open("IntermediateFiles/final2Graph.txt", "w")
    totalText = doc.read()
    for positive in positivePriors:
        totalText = totalText.replace(positive + ',', positive + '*' + ',')
    for negative in negativePriors:
        totalText = totalText.replace(negative + ',', negative + '^' + ',')
    doc2.write(totalText)
    doc.close()
    doc2.close()

def finalFinalProcessing():
    backEdges = dict()
    doc = open("IntermediateFiles/final2Graph.txt", "r")
    for line in doc:
        a, rest = line.split('\t', 1)
        b, c, d, e = rest.split('|', 3)
        for word in b.split(','):
            if len(word.strip()) > 0:
                if word.strip() in backEdges:
                    backEdges[word.strip()].append(a.strip())
                else:
                    backEdges[word.strip()] = [a]
    #print backEdges['colour']
    doc.close()
    doc = open("IntermediateFiles/final2Graph.txt", "r")
    doc2 = open("OutputFiles/finalGraph.txt", "w")
    for line in doc:
        contains = []
        a, rest = line.split('\t', 1)
        b, c, d, e = rest.split('|', 3)
          
        for word in b.split(','):
            if (len(word.strip())> 0) & (word.strip() not in contains):
                contains.append(word.strip())
        if a.strip() in backEdges:
            for backEdge in backEdges[a.strip()]:
                if backEdge.strip() not in contains:
                    contains.append(backEdge.strip())
                    #newB += (backEdge.strip() + ',')
        newB = str(contains).replace('[', ' ').replace(']', ' ').replace("'", ' ')
        newLine = a + ' \t ' + newB + ' | ' + c + ' | ' + d + ' | ' + e
        #line.replace(b, ' ' + newB + ' ')
        doc2.write(newLine)
    doc2.close()
    doc.close()



               
runAll()
