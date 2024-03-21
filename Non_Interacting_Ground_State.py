import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import subprocess

# Input information (system size, number of flavors ...)
# dimension = int(input("dimensionality = ? \n"))
dimension = 2

d_array = np.empty(dimension,dtype=np.int64)
"""
for d in range(dimension):
  d_array[d] = int(input("How many sites in direction {} ? \n".format(d)))
"""

# template
d_array[0] = 3
d_array[1] = 3
#d_array[2] = 2

L = np.prod(d_array)
print("We are studying a {}-dimensional lattice with {} sites \n\n".format(dimension,L))

# ibc = int(input("Please enter 0 for PBC and 1 for OBC \n"))
ibc = 0

# N = int(input("number of flavors = ? \n"))
N = 1

M = N*L
print("The dimension of the single particle Hilbert space is {} \n\n".format(M))
print("I will now generate the hamiltonian for one particle ... \n\n ")

#generate the hamiltonian for one particle of a given flavor
def coor(index,d,n,Ns):
    den=Ns; coor=np.empty(d, dtype=int)
    for i in range(d-1, -1, -1):
        den/=n[i]
        coor[i]=index/den
        index%=den
    return coor

def coor_to_index(coor, d, d_array):
    index = 0
    m = 1
    #print(d-1)
    for dim in range(d):
        index = index + m*coor[dim]
        m = m*d_array[dim] 
    return index 

# Hamiltoian 
Honey = np.zeros(L*L,dtype=np.complex128)
site_i = []; site_j = []; hopping = []
for i in range(L): #loop over the lattice sites
   #find the d coordinates of site i
   coor_i = coor(i,dimension,d_array,L)
   #test coordinates and labels
   print("coordinate {}: ".format(i), coor_i)
   j = coor_to_index(coor_i, dimension, d_array)
   print("label {}: \n\n".format(j))
   #find the 2d nearest neighbors of site i
   for dim in range(dimension):
      for nn in (-1,1):
        coor_j = deepcopy( coor_i )
        coor_j[dim] = coor_i[dim] + nn
        if(ibc == 0): #PBC
          if(coor_j[dim] < 0):
            coor_j[dim] = coor_j[dim] + d_array[dim]
          if(coor_j[dim] > d_array[dim]-1):
            coor_j[dim] = coor_j[dim] - d_array[dim]          
          print("*** nearest neighbor found in ", coor_j)
          j = coor_to_index(coor_j, dimension, d_array)
          print("*** nn label {}:".format(j))
   print("\n\n")

Honey = Honey.reshape((L, L))
print(Honey.size)
eigenvalues, eigenvectors = np.linalg.eigh(Honey)









