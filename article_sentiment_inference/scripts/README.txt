Code in WordValuePreprocessing requires installation of a .exe thesaurus. (Wordnet) 

Doing:
sh runningScript.sh

Will run all the rest of the code. (Running each piece, copying output to input as needed) 
Needed files for the LDA + topic classification will be placed in LDAFiles. Results placed in folder Final_Results; they include

1) fullResults.txt, which contains articles and ratings. Each article is enclosed in a tuple: 
(Article index, words identified, scores of words identified, method 1 score, method 2 score, method 3 score, original text)  

2) valueDictionary.txt, which contains words and their ratings. 

3) topics.txt, which contain the topics found by LDA.

4) topicratings.txt, the pre-scaled ratings for the topics.

5) top.txt, the top 10 documents contributing to the rating for each topic.

Input to the entire program can be found in WordValuePreprocessing/InputFiles/Articles, which contains
the RSS articles in their original form. 

Note that other than the InputFiles/OutputFiles folders of WordValuePreprocessing (Which has already been run for you) 
the InputFiles/OutputFiles of each part are blank, just do the command above once will fill them in, 
along with the folders LDAFiles and Final_Results. (This is to demonstrate our code indeed works) 

Topic_Inference directory contains all the Matlab code necessary to run the LDA inference and output topics.txt, 
topicratings.txt, and top.txt. Putting the files from LDAFiles in the same directory and running topicinference.m 
will output the desired results. WriteTopics.m and GibbsSamplerLDA.m are intermediate files used by topicinference.m. 
Note: we used the Matlab package at http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm to run our inference.

Result text files can also be found in https://sites.google.com/site/articleinference/documents

See https://sites.google.com/site/articleinference/application-usage for more details.