from input_handler import get_user_input
from hamiltonian_generator import define_hamiltonian, periodic_hamiltonian_NI, periodic_hamiltonian_I, open_hamiltonian_NI, open_hamiltonian_I

d, f, d_a, ibc =  get_user_input()
H = define_hamiltonian(f,d_a)
