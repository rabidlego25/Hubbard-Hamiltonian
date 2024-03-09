import numpy as np

def get_user_input():
	"""
	Asks the user for model parameters and returns them
	
	Returns:
	dimensionality: Int, Total Dimensions of the lattice (ie 1D, 2D, 3D)
	flavors: Int, Unique characteristic of a particle like spin
	d_array: List, Holds the total sites in each dimension of the array
	ibc: String, Specifies whether the particle is susceptible to open or periodic boundary conditons 
	"""
	print("I will now ask for the model parameters\n")

	# Dimensionality of the lattice
	dimensionality = int(input("Dimensionality of the lattice?\n"))

	# Number of Flavors
	flavors = int(input("Number of flavors?\n"))

	# Size of the lattice
	d_array = np.zeros(dimensionality, dtype=int)
	for i in range(dimensionality):
		d_array[i] = int(input(f"Please enter points in the {i} direction:\n"))	

	# Boundary Conditions
	ibc = input("Boundary conditions (open 0, periodic 1)?\n")
	while ibc not in ["0", "1"]:
		print("Input Error! Please enter a 0 for open and 1 for periodic!!\n")
		ibc = input("Boundary conditions (open 0, periodic 1)?")
	boundary_condition = "open" if ibc == "0" else "periodic"

	# Printing the Specs
	print("\nLattice Constructed")
	print(f"Dimension: {dimensionality}\nTotal Sites: {d_array.prod()}\nFlavors: {flavors}\nBoundary Condition: {boundary_condition}\n")
	
	return dimensionality, flavors, d_array, ibc

def interacting():
	"""
	Ascertain if the user will pursue the interacting or non-interacting model
	
	Returns:
	is_interacting: String, Specifies whether the system encompasses the interacting or non-interacting case
	"""

	is_interacting = input("Interacting (no 0, yes 1)?\n")
	while is_interacting not in ["0", "1"]:
		print("Input Error! Please enter a 0 for no and 1 for yes!\n")
		ibc = input("Interacting (no 0, yes 1)?")

	return is_interacting
