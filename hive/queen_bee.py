from input_handler import get_user_input
from hamiltonian_generator import define_hamiltonian

d, f, d_a, ibc, num_p, is_i  =  get_user_input()
H = define_hamiltonian(f,d_a,num_p)

print(H)
