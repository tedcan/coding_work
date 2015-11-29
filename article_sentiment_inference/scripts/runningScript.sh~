#!/bin/bash

cp WordValuePreprocessing/OutputFiles/finalGraph.txt ModifiedPageRank/InputFiles/finalGraph.txt
cp WordValuePreprocessing/OutputFiles/originalArticles.txt Article_Classifying/InputFiles/originalArticles.txt
cp WordValuePreprocessing/OutputFiles/parsedArticles.txt Article_Classifying/InputFiles/parsedArticles.txt
cp WordValuePreprocessing/OutputFiles/parsedArticles.txt LDA_Formatting/InputFiles/parsedArticles.txt

sh ModifiedPageRank/run.sh

cp ModifiedPageRank/OutputFiles/valueDictionary.txt Article_Classifying/InputFiles/valueDictionary.txt

python Article_Classifying/classify.py
python LDA_Formatting/ldaformat.py

cp LDA_Formatting/OutputFiles/ArticleAssignmentVector.txt LDAFiles/ArticleAssignmentVector.txt
cp LDA_Formatting/OutputFiles/ArticleWordVector.txt LDAFiles/ArticleWordVector.txt
cp LDA_Formatting/OutputFiles/UniqueWordsVector.txt LDAFiles/UniqueWordsVector.txt
cp Article_Classifying/OutputFiles/shortResultsForLDA.txt LDAFiles/shortResultsForLDA.txt

cp ModifiedPageRank/OutputFiles/valueDictionary.txt Final_Results/valueDictionary.txt
cp Article_Classifying/OutputFiles/fullResults.txt Final_Results/fullResults.txt
