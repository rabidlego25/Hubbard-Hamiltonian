import numpy as np

def get_user_input():
	"""
	Asks the user for model parameters and returns them. The intention is to acquire all of the Specs of the system.
	
	Returns:
	dimensionality: Int, Total Dimensions of the lattice (ie 1D, 2D, 3D)
	flavors: Int, Unique characteristic of a particle like spin
	d_array: List, Holds the total sites in each dimension of the array
	ibc: String, Specifies whether the particle is susceptible to open or periodic boundary conditons 
	num_particles (int): total number particles in the system
	"""
	print("I will now ask for the model parameters\n")

	# Number of particles in the System
	num_particles = int(input("Please enter total particles in the system\n"))

	# Dimensionality of the lattice
	dimensionality = int(input("Dimensionality of the lattice?\n"))

	# Number of Flavors
	flavors = int(input("Number of flavors?\n"))

	# Size of the lattice
	d_array = np.empty(dimensionality, dtype=np.int64)
	for i in range(dimensionality):
		d_array[i] = int(input(f"Please enter points in the {i} direction:\n"))	

	# Boundary Conditions
	ibc = input("Boundary conditions (open 0, periodic 1)?\n")
	while ibc not in ["0", "1"]:
		print("Input Error! Please enter a 0 for open and 1 for periodic!!\n")
		ibc = input("Boundary conditions (open 0, periodic 1)?")
	boundary_condition = "open" if ibc == "0" else "periodic"

	# Interacting
	
	is_interacting = input("Interacting (no 0, yes 1)?\n")
	while is_interacting not in ["0", "1"]:
		print("Input Error! Please enter a 0 for no and 1 for yes!\n")
		is_interacting = input("Interacting (no 0, yes 1)?")

	# Printing the Specs
	print("\nLattice Constructed")
	print(f"Dimension: {dimensionality}\nTotal Sites: {d_array.prod()}\nFlavors: {flavors}\nBoundary Condition: {boundary_condition}\nIs Interacting: {is_interacting}")
	
	return dimensionality, flavors, d_array, ibc, num_particles, is_interacting
