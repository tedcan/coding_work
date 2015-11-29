totalList = []
w = open('ModifiedPageRank/OutputFiles/FinalOutputFile.txt', 'r')
r = open('ModifiedPageRank/OutputFiles/valueDictionary.txt', 'w')
for line in w.readlines():
	line = line.replace('"', '')
	word, rest = line.split('\t', 1)
	a, meaning, c, d = rest.split('|', 3)
	newTuple = (word.strip(), float(meaning))
	totalList.append(newTuple)

totalList = sorted(totalList, key=lambda entry: entry[1])

for i in range(len(totalList)): 
	r.write(str(totalList[i]) + '\n')

w.close()
r.close()
