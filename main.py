# Converts ASCII strings to binary (base two)

def convert(string):
	string_to_bytearray = bytearray(string, 'utf8')
	binary_array = []
	
	for byte in string_to_bytearray:
		bin_rep = bin(byte)[2:].zfill(8)
		binary_array.append(bin_rep)

	return binary_array

print_bin = lambda arr: ' '.join([str(bin) for bin in arr])