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
d_array[0] = 6
d_array[1] = 4
#d_array[2] = 2

L = np.prod(d_array)
print("We are studying a {}-dimensional lattice with {} sites \n\n".format(dimension,L))

# ibc = int(input("Please enter 0 for PBC and 1 for OBC \n"))
ibc = 0

# N = int(input("number of flavors = ? \n"))
N = 3
Npart = np.empty(N,dtype=np.int64)
Npart[0] = 5
Npart[1] = 5
Npart[2] = 5

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
t = -1
site_i = []; site_j = []; hopping = []

if(ibc == 0): #PBC
  for i in range(L): #loop over the lattice sites
    #find the d coordinates of site i
    coor_i = coor(i,dimension,d_array,L)
    #print("coordinate {}: ".format(i), coor_i)
    #find the nearest neighbors of site i
    for dim in range(dimension):
      for nn in (-1,1):
        coor_j = deepcopy( coor_i )
        coor_j[dim] = coor_i[dim] + nn
        if(coor_j[dim] < 0):
          coor_j[dim] = coor_j[dim] + d_array[dim]
        if(coor_j[dim] > d_array[dim]-1):
          coor_j[dim] = coor_j[dim] - d_array[dim]
        #print("*** nearest neighbor found in ", coor_j)
        j = coor_to_index(coor_j, dimension, d_array)
        #print("*** nn label {}:".format(j))
        site_i.append(i)
        site_j.append(j)
        hopping.append(t)
elif(ibc == 1): #OBC
  for i in range(L): #loop over the lattice sites
    coor_i = coor(i,dimension,d_array,L)
    for dim in range(dimension):
      if(coor_i[dim] == 0):
        coor_j = deepcopy( coor_i )
        coor_j[dim] = coor_i[dim] + 1
        j = coor_to_index(coor_j, dimension, d_array)
        #print("*** nearest neighbor found in ", coor_j)
        #print("*** nn label {}:".format(j))
        site_i.append(i)
        site_j.append(j)
        hopping.append(t)
      elif(coor_i[dim] == d_array[dim]-1):
        coor_j = deepcopy( coor_i )
        coor_j[dim] = coor_i[dim] - 1
        j = coor_to_index(coor_j, dimension, d_array)
        #print("*** nearest neighbor found in ", coor_j)
        #print("*** nn label {}:".format(j))
        site_i.append(i)
        site_j.append(j)
        hopping.append(t)
      else:
        for nn in (-1,1):
          coor_j = deepcopy( coor_i )
          coor_j[dim] = coor_i[dim] + nn
          j = coor_to_index(coor_j, dimension, d_array)
          #print("*** nearest neighbor found in ", coor_j)
          #print("*** nn label {}:".format(j))
          site_i.append(i)
          site_j.append(j)
          hopping.append(t)

print("\n\n")

#for i in range(len(site_i)):
 # print("Pair of nn sites ({}, {}) \n".format(site_i[i],site_j[i]))
   
Honey = np.zeros((L,L),dtype=np.complex128)
#print(Honey.size)

nhoppings = len(hopping)
for hop in range(nhoppings):
  Honey[site_i[hop],site_j[hop]] = hopping[hop]
	#hopping would be the -t term in the hamiltonian

myfile = open("1B_Hamiltonian_One_Flavor.info","w")
for i in range(L):
  for j in range(L):
     myfile.write("{} {} {} {} \n".format(i,j,np.real(Honey[i,j]),np.imag(Honey[i,j])))
myfile.close()

#diagonalize the one-body hamiltonian for one flavor
eigenvalues, eigenvectors = np.linalg.eigh(Honey)
myfile = open("1B_Eigenvalues.info","w")
for i in range(L):
  myfile.write("{} {} \n".format(i,eigenvalues[i]))
myfile.close()

print(eigenvectors)
myfile = open("1B_Eigenvectors.info","w")
for i in range(L):
	myfile.write(f"{i} {eigenvectors[i]}\n\n")
myfile.close()

#build the wave functions for the different Flavors
ncols = int(np.max(Npart))
Psi = np.empty((L,ncols,N),dtype=np.complex128)

for flav in range(N):
  myfile = open("WaveFunction_Flavor"+str(flav)+".info","w")
  myfile.write("# particle, site, Re(Psi), Im(Psi) \n")
  for part in range(Npart[flav]):
    for site in range(L):
      Psi[site,part,flav] = eigenvectors[site,part]
      myfile.write("{} {} {} {} \n".format(part,site,np.real(Psi[site,part,flav]),np.imag(Psi[site,part,flav])))
  myfile.write("\n\n")
  myfile.close()
