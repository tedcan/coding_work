function coeff = find_coeff(data, dim)

[v,d] = eigs(data'*data,dim);

%[v,d] = eig(data'*data);
%v = v(:,1:dim);

coeff  = v;