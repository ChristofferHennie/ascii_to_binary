# Converts ASCII strings to binary (base two)
import binascii

def convert_to_binary(string):
	string_to_bytearray = bytearray(string, 'utf8')
	binary_array = []
	
	for byte in string_to_bytearray:
		bin_rep = bin(byte)[2:].zfill(8)
		binary_array.append(bin_rep)

	return binary_array

def convert_to_string(in_bytes):
  values = in_bytes.split(' ')
  string_array = []

  for value in values:
    intager = int(value, 2)
    character = chr(intager)
    string_array.append(character)
  
  return string_array


print_bin = lambda arr: ' '.join(arr)

a = print_bin(convert_to_binary('Halla'))

print(a)
print(''.join(convert_to_string(a)))

