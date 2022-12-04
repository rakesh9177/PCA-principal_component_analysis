import numpy as np


def pca(X,n_components=2):
  cov = np.cov(x.T). #Getting the covariance matrix of the feature space
  print(cov.shape)
  eigen_values, eigen_vectors= np.linalg.eigh(cov)
  required_ev = eigen_vectors[:,-2:]
  for i in range(n_components):
    nm = np.linalg.norm(required_ev[:,i])
    required_ev[:,i]= ((1/nm)*required_ev[:,i])
  print(required_ev.shape)
  return np.matmul(required_ev.T,X.T)
