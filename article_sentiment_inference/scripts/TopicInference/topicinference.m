clear all

% WS a 1 x N vector where WS(k) contains the vocabulary index of the kth 
% word token, and N is the number of word tokens. The word indices are not 
% zero based, i.e., min(WS)=1 and max(WS)=W=number of distinct words 
% in vocabulary
WS = importdata('ArticleWordVector.txt');

% DS a 1 x N vector where DS(k) contains the document index of
% the kth word token. The document indices are not zero based, i.e., 
% min(DS)=1 and max(DS)=D=number of documents
DS = importdata('ArticleAssignmentVector.txt');

% WO a 1 x W cell array of strings where WO{k} contains the kth
% vocabulary item and W is the number of distinct vocabulary items.
% Not needed for running the Gibbs sampler but becomes necessary
% when writing the resulting word-topic distributions to a file
% using the writetopics matlab function.
WO = importdata('UniqueWordsVector.txt');

% ratings is a 1 x D array where ratings(i) is the rating of the
% ith document as obtained from page rank
results = importdata('shortResultsForLDA.txt');
temp = sortrows(results,1);
ratings = temp(:,2);


% number of topics
T = 10;

% hyperparameters for Dirichlet priors
beta = 0.01;
alpha = 1;

% number of iterations
n = 500;

% random seed for the random number generator
seed = 3;

% what debug outputs to show (0=no output; 1=iterations; 2=all output)
debug = 1;

% running the actual LDA Gibbs sampler, tic-toc for timing
tic
[WP,DP,Z] = GibbsSamplerLDA(WS, DS, T, n, alpha, beta, seed, debug);
toc

% Write the topics to a text file
WriteTopics(WP, beta, WO, 10, 0.7, 4, 'topics.txt');


% to calculate the rating of each topic
topicratings = zeros(1,T);
for i=1:T
    % get the ids of documents which has at least one word assigned to
    % topic i
    docIds = find(DP(:,i));
    % total number of words assigned to topic i
    tot = sum(DP(:,i));
    % loop through all docs which has some word assigned to topic i and add
    % the weighted contribution of a doc to the rating of topic i based on
    % how many words were assigned to topic i from the doc
    for j=1:length(docIds)
        topicratings(i) = topicratings(i) + (DP(docIds(j),i)/tot)*ratings(docIds(j));
    end
end
% write the topicratings to topicratings.txt
dlmwrite('topicratings.txt',topicratings,'delimiter','\t','precision',4);

% find the 10 indices of documents that contribute the most to each topic
% top(i,:) will be the top 10 indices of topic i
top = zeros(10);
for i=1:T
    [vals, inds] = sort(DP(:,i),'descend');
    top(i,:) = inds(1:10);
end
% write the top 10 indices to top.txt
dlmwrite('top.txt',top,'delimiter','\t');
