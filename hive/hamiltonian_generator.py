import numpy as np

def define_hamiltonian(f, d_a, n):
	"""
	Constructs generic hamiltonian
	
	Parameters
	f (int), total number of flavors
	d_a (list of ints),  Number of total sites in each direction of the lattice
	n (int), total number of particles

	Returns
	H: Undiagonalized Hamiltonian Matrix
	"""
	L = np.prod(d_a)
	H = np.zeros((L*f*n,L*f*n), dtype=np.complex128)
	print(f"Hamiltonian matrix with {L*f*n} x {L*f*n} dimensionality constructed") 
	return H

def find_nearest_neighbors(H, H_dim):
	for i in range(H_dim):
		i = 1
	return

def add_kinetic_term():
	return

def add_potential_term():
	return

def coor(i,d,d_a,l):
	"""
	Takes a index in a n-dimensional lattice and transforms it into a coordinate

	Parameters
	i (int), index of interest
	d (int), total dimensionality
	d_a (1D np array), total sites in each dimension
	l (int), length in 1 direction
		
	Returns
	coor (1D array of length 
	"""
	den = Ns; coor = np.empty(d,dtype=int)
	for i in range(d-1,-1,-1):
		den /= n[i]
		coor[i] = index/den
		index %= den
	return coor

def coor_to_index(coor, d, d_array):
	index = 0
	m = 1
	for dim in range(d):
		index = index + m*coor[dim]
		m = m*d_array[dim]
	return index
