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
U = float("Enter the value of U")

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

# diagonalize
eigval, eigvec = np.linalg.eigH(H)
