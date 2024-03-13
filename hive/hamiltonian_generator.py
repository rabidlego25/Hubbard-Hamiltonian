import numpy as np

def define_hamiltonian(f, d_a):
	"""
	Constructs generic hamiltonian
	
	Parameters
	f (int), total number of flavors
	d_a (list of ints),  Number of total sites in each direction of the lattice

	Returns
	H: Undiagonalized Hamiltonian Matrix
	"""
	L = np.prod(d_a)
	H = np.zeros((L*f,L*f), dtype=np.complex128)
	print(f"Hamiltonian matrix with {L*f} x {L*f} dimensionality constructed") 
	return H

def periodic_hamiltonian_NI():
	"""
	Constructs a hamiltonian with periodic boundary conditions with a focus on the non-interacting case
	"""
	return

def periodic_hamiltonian_I():
	"""
	Constructs a hamiltonian with periodic boundary conditions with a focus on the interacting case
	"""
	return

def open_hamiltonian_NI():
	"""
	Constructs a hamiltonian with open boundary conditions with a focus on the non-interacting case
	"""
	return

def open_hamiltonian_I():
	"""
	Constructs a hamiltonian with open boundary conditions with a focus on the interacting case
	"""
	return
