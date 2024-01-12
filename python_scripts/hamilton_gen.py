import numpy as np
import matplotlib.pyplot as plt

"""
e_0 = c^{\dagger}_{0,up} c^{\dagger}_{0,dn} |0>
e_1 = c^{\dagger}_{0,up} c^{\dagger}_{1,dn} |0>
e_2 = c^{\dagger}_{0,dn} c^{\dagger}_{1,up} |0>
e_3 = c^{\dagger}_{1,up} c^{\dagger}_{1,dn} |0>
"""

H = np.empty((4,4),dtype=np.complex128)

t = 1.0
# U = float(input("Enter the value of U"))
U = float(1)

# define the hamiltonian
H[0,0] = U
H[0,1] = -t
H[0,2] = t
H[0,3] = 0
H[1,0] = -t
H[1,1] = 0
H[1,2] = 0
H[1,3] = -t
H[2,0] = t
H[2,1] = 0
H[2,2] = 0
H[2,3] = t
H[3,0] = 0
H[3,1] = t
H[3,2] = t
H[3,3] = U

print('Hamiltonian constructed\nSites: 2 \nBoundary: periodic\nPauli exclusion: yes\n')

# diagonalize
eigval, eigvec = np.linalg.eigh(H)

# display eigenvalues
"Here are the eigenvalues associated with the system: \n\n "
for i in range(4):
	print(f'eigenvalue {i+1}: {round(eigval[i])}')

# lowest energy eigenstates of the hamiltonian
for i in range(4):
	print(f'eigenstate {i+1}: {round(eigvec[i,0].real,3)}+{eigvec[i,0].imag}j')

# defining the square modulus
def sqmod(z):
	a = np.real(z)
	b = np.imag(z)
	return a**2 + b**2

print('probability to observe up/dn empty  {} \n'.format(sqmod(eigvec[0,0])))
print('probability to observe up    dn     {} \n'.format(sqmod(eigvec[1,0])))
print('probability to observe dn    up     {} \n'.format(sqmod(eigvec[2,0])))
print('probability to observe empty up/dn  {} \n\n'.format(sqmod(eigvec[3,0])))


# display eigenvectors
print('Eigenvectors of H \n')
for n in range(4):
	print(f'|psi_{n}> = \n')
	for i in range(4):
		re = np.real(eigvec[i,n])
		im = np.imag(eigvec[i,n])
		print(f'+( {round(re,3)}, {im} ) e_{i}')
	print("\n\n")

# time-dependent Schroedinger equation \n\n
