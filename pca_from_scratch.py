import numpy as np


def pca(X,n_components=2):
  #Getting the covariance matrix of the feature space
  cov = np.cov(x.T). 
  #get the eigen_values and eigen_vectors of the covariance matrix
  #eigh will give eigen values and its associated eigen vectors in ascending order of eigen values
  eigen_values, eigen_vectors= np.linalg.eigh(cov)
  
  #for pca , we need eigen vectors associated with top n_component eigen vectors i.e for 2 components, we need eigen vectors of top 2 eigen values
  required_ev = eigen_vectors[:,-2:]
  
  #Normalize the eigen vector using norm, if v is a vector, it's normalized form is v/|v|
  for i in range(n_components):
    nm = np.linalg.norm(required_ev[:,i])
    required_ev[:,i]= ((1/nm)*required_ev[:,i])
 
  # returning n principal components, by default it's 2, therefore it returns two principal components, PC1 = normalized_vector.Transpose x Data.Transpose
  return np.matmul(required_ev.T,X.T)
