#!/usr/bin/env python3
import sys
import socket


def encrypt(msg, pad):
	# both msg and pad are byte arrays
	ciphertext = bytearray(len(msg))

	# write code here

	return ciphertext


def decrypt(ciphertext, pad):
	# both msg and pad are byte arrays
	msg = bytearray(len(ciphertext))

	# write code here

	return msg



def main(argv):
	msg = argv[1]
	pad = argv[2]

	print("Plain message:")
	print(msg)
	print("\nPad:")
	print(pad)

	cipher = encrypt(msg.encode(), pad.encode())

	print("\nCipher text (as integer array):")
	print(list(cipher))

	decoded = decrypt(cipher, pad.encode())

	print("\nDecoded text (as integer array):")
	print(list(decoded))
	print("\nDecoded plain text:")
	print(decoded.decode())



# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s msg pad' % sys.argv[0])
	else:
		main(sys.argv)
