import os
import string
import re

IndicesToWords = dict()
uniqueWordsToIndices = dict()

wordsToEliminate = ['that', 'would', 'from', 'will', 'this', 'with', 'they', 'than',
                    'have', 'into', 'about', 'make', 'which', 'them', 'their', 'what',
                    'only', 'take', 'when', 'where', 'after']

def runAll():
    getWordVector()
    getArticleVector()

def getWordVector():
    f = open('LDA_Formatting/InputFiles/parsedArticles.txt', 'r')
    counter = 1
    for line in f.readlines():
        for word in line.split(' '):
            word = word.strip()
            allLetters = 1
            if (len(word) > 3) & (word not in wordsToEliminate):
                for character in word:
                    if not character.isalpha():
                        allLetters = 0
                    if allLetters > 0:           
                        if word not in uniqueWordsToIndices:
                            uniqueWordsToIndices[word] = counter
                            IndicesToWords[counter] = word
                            counter += 1
    f.close()
    g = open('LDA_Formatting/OutputFiles/UniqueWordsVector.txt', 'w')
    for i in range(len(IndicesToWords)):
        g.write(IndicesToWords[i + 1] + '\n')

def getArticleVector():
    
    f = open('LDA_Formatting/InputFiles/parsedArticles.txt', 'r')
    w1 = open('LDA_Formatting/OutputFiles/ArticleWordVector.txt', 'w')
    w2 = open('LDA_Formatting/OutputFiles/ArticleAssignmentVector.txt', 'w')

    w1vector = []
    w2vector = []
    counter = 1
    for line in f.readlines():
        for word in line.split(' '):
            if word in uniqueWordsToIndices:
                w1vector.append(uniqueWordsToIndices[word])
                w2vector.append(counter)
        counter += 1
    w1vector = str(w1vector).replace('[', '').replace(']', '').replace("'", '')
    w2vector = str(w2vector).replace('[', '').replace(']', '').replace("'", '')
    w1.write(w1vector)
    w2.write(w2vector)
    w1.close()
    w2.close()
    f.close()

runAll()
