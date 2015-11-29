import os
import string
import re
import math
import numpy

article_dict = dict()
conn_dict = dict()
overall_article_list = []

def scale(highest, least, newhigh, newleast, number):
    #halfway = abs(highest - least)
    #shift = 0
    #if abs(highest) > abs(least):    
    #    shift = highest - halfway / 2
    #elif abs(least) > abs(highest):
    #    shift = least + halfway / 2
    #return (number - shift) * (newhigh - newleast) / (highest - least)
    return number * (newhigh - newleast) / (highest - least)

def analyze_performance(indices):
    
    methods = ['Standard Average Method', 'Modified Average Method', 'Median Evaluation Method']
    f2 = open('Article_Classifying/OutputFiles/test_performance.txt', 'w')
    counter = 0
    for indice in indices:
        f = open('Article_Classifying/InputFiles/test_set.txt', 'r')
        samples = 0
        total_difference = 0.0
        total_sameside = 0.0
        positive = 0.0
        positive_actual = 0.0
        negative = 0.0
        negative_actual = 0.0
        zero_actual = 0.0
        positive_count  = 0.0
        negative_count = 0.0
        for entry in f.readlines():
            article, score = entry.split(',', 1)
            article = int(article)
            score = float(score)
            hypothesis = article_dict[article][indice]
            #if indice == 3:
                #print "new entry"
                #print article
                #print score
                #print hypothesis
            total_difference += abs(score - hypothesis)
            samples += 1
            if hypothesis >= 0:
                positive_count += 1
            if hypothesis < 0:
                negative_count += 1
            if (hypothesis >= 0) & (score >= 0):
                total_sameside += 1
            if (hypothesis > 0) & (score > 0):
                positive += 1
            if score > 0:
                positive_actual += 1
            if (hypothesis < 0) & (score < 0):
                total_sameside += 1
                negative += 1
            if score < 0:
                negative_actual += 1
            if score == 0:
                zero_actual += 1
        average_difference = total_difference / samples
        percent_sameside = total_sameside / samples

        if counter == 0:
            f2.write("Size 100 test data statistics: " + '\n')
            f2.write( "Zero Actual Cases: " + str(zero_actual) + '\n')
            f2.write(  "Positive Actual Cases: " + str(positive_actual) + '\n')
            f2.write(  "Negative Actual Cases: " + str(negative_actual) + '\n\n')
        
        f2.write( methods[counter] + '\n')
        counter += 1
        f2.write(  "Positive Classified Cases: " + str(positive_count) + '\n')
        f2.write(  "Negative Classified Cases: " + str(negative_count) + '\n')
        f2.write(  "Average difference: " + str(average_difference) + '\n')
        f2.write(  "Percentage on same side of the test data: " + str(percent_sameside) + '\n')
        f2.write(  "Percent of positive articles classified on the same side: " + str(positive/positive_actual) + '\n')
        f2.write(  "Percent of negative articles classified on the same side: " + str(negative/negative_actual) + '\n\n')
        f.close()
    f2.close()
    
def runAll():
    f2 = open('Article_Classifying/OutputFiles/shortResultsForLDA.txt', 'w')
    f = open('Article_Classifying/OutputFiles/fullResults.txt', 'w')
    obtainScoring()
    sorted_overall_article_list1 = extreme_rated(3)
    highest1 = sorted_overall_article_list1[len(sorted_overall_article_list1) - 1][3]
    lowest1 = sorted_overall_article_list1[0][3]

    sorted_overall_article_list2 = extreme_rated(4)
    highest2 = sorted_overall_article_list2[len(sorted_overall_article_list2) - 1][4]
    lowest2 = sorted_overall_article_list2[0][4]

    sorted_overall_article_list3 = extreme_rated(5)
    highest3 = sorted_overall_article_list3[len(sorted_overall_article_list3) - 1][5]
    lowest3 = sorted_overall_article_list3[0][5]
    
    new_sorted_overall_article_list = []

    for entry in sorted_overall_article_list1:
        newScore1 = 0
        newScore2 = 0
        newScore3 = 0 
        if entry[3] < 0:
            newScore1 = scale(0, lowest1, 0, -2, entry[3])
            newScore2 = scale(0, lowest2, 0, -2, entry[4])
            newScore3 = scale(0, lowest3, 0, -2, entry[5])
        else:
            newScore1 = scale(highest1, 0, 2, 0, entry[3])
            newScore2 = scale(highest2, 0, 2, 0, entry[4])
            newScore3 = scale(highest3, 0, 2, 0, entry[5])

            
        #newScore1 = scale(highest1, lowest1, 2, -2, entry[3])
        #newScore2 = scale(highest2, lowest2, 2, -2, entry[4])
        #newScore3 = scale(highest3, lowest3, 2, -2, entry[5])
        newEntry = (entry[0], entry[1], entry[2], newScore1, newScore2, newScore3, entry[6])
        new_sorted_overall_article_list.append(newEntry)
        article_dict[entry[0]] = newEntry
        #print newScore1
    for entry in new_sorted_overall_article_list:
        f.write(str(entry) + '\n')
        # + 1 since Matlab is indiced from 1. 
        f2.write(str(entry[0] + 1) + ', '  + str(entry[4]) + '\n')
    f.close()
    f2.close()
    analyze_performance([3,4,5])
    
        
def obtainScoring():

    articles = open('Article_Classifying/InputFiles/originalArticles.txt', 'r')
    formattedArticles = open('Article_Classifying/InputFiles/parsedArticles.txt', 'r')
    connotations = open('Article_Classifying/InputFiles/valueDictionary.txt', 'r')

    counter = 0
    for line in articles.readlines():
        article_dict[counter] = line
        counter += 1

    for line in connotations.readlines():
        line = line.strip()
        line = line.replace("'", "")
        line = line.replace(")", "")
        line = line.replace("(", "")
        #line = line.replace("*", "")
        #line = line.replace("^", "")
        word, value = line.split(",", 1)
        if (value > 0.06 ) | (value < 0.0): 
            conn_dict[word.strip()] = float(value)
    counter2 = 0
    for line in formattedArticles.readlines():
        articleScore = 0
        numberIdentified = 0
        wordsMarked = []
        scores = []
        for word in line.split(' '):
            if (len(word.strip()) > 0) & (word.strip() in conn_dict):
                numberIdentified += 1
                articleScore += conn_dict[word]
                wordsMarked.append(word)
                scores.append(conn_dict[word])
        if numberIdentified > 0:        
            overall_article_list.append((counter2, wordsMarked, scores, articleScore / len(wordsMarked),
                                         articleScore / math.sqrt(float(len(wordsMarked))),
                                         numpy.median(scores),
                                         article_dict[counter2]))
            article_dict[counter2] = (counter2, wordsMarked, scores, articleScore / len(wordsMarked),
                                      articleScore / math.sqrt(float(len(wordsMarked))),
                                      numpy.median(scores),
                                    article_dict[counter2])
        else:
            overall_article_list.append((counter2, wordsMarked, scores, 0, 0, 0,
                                         article_dict[counter2]))
            article_dict[counter2] = (counter2, wordsMarked, scores, 0, 0, 0,
                                      article_dict[counter2])
        counter2 += 1

    articles.close()
    formattedArticles.close()
    connotations.close()


def extreme_rated(indice):
    return sorted(overall_article_list, key=lambda entry: entry[indice])
    
runAll()

