%function estimated_scores = pca_2d(data, itemDim, userDim)

data = itemMatrix;
itemDim = 8;
userDim = 8; 

data = data-mean(mean(data));   %de-mean the data matrix



%data is a de-meaned 0-1 matrix with I rows and U users.  


numberOfItems = length(data(:,1));
numberOfUsers = length(data(1,:));



score = zeros(numberOfItems, numberOfUsers);
estimated_scores = zeros(numberOfItems, numberOfUsers);

coeff = find_coeff(data,userDim);
coeffT = find_coeff(data',itemDim);

%coeff = find_coeff_pca(data,userDim);
%coeffT = find_coeff_pca(data', itemDim);



%compute the scores for the PC's 

for i = 1:itemDim
    for j = 1:userDim
      temp =0 ;
      for k = 1:numberOfItems 
        for r = 1:numberOfUsers
            temp = temp+data(k,r)*coeffT(k,i)*coeff(r,j);
        end 
      end 
      score(i,j) = temp;
     end 
end  

   
%Compute the scores for the main matrix from the matrix of scores for the
%PC's 


for i = 1:numberOfItems
    for j = 1:numberOfUsers
       temp = 0;
         for k = 1:itemDim    %number of pca dimensions of the items 
          for r = 1:userDim    % number of pca dimensions of the users 
              temp = temp+score(k,r)*coeffT(i,k)*coeff(j,r);
          end 
         end 
        estimated_scores(i,j) = temp;
    end 
end 