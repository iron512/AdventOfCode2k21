#!/usr/bin/env python3

import time
	
def char2hex(char):
	return str(bin(int(char, 16))[2:].zfill(4))

def hex2int(hexn):
	final = 0
	length = len(hexn)
	for digit in range(length):
		final += int(hexn[digit])*pow(2,length-1-digit)
	return final

def hex2char(hexn):
	return str(hex(hex2int(hexn)))[2].upper()

def main():
	data = open("input.txt","r").read()
	data = open("test1.txt","r").read()
	data = open("test2.txt","r").read()
	data = open("test3.txt","r").read()
	data = "38006F45291200"

	translation = [""]
	for char in data:
		translation[0] += char2hex(char)

	total = 0
	while len(translation) != 0: 
		study = translation.pop()
		version = hex2int(study[0:3])
		packtype = hex2int(study[3:6])

		total += version
		study = study[6:-1]+study[-1]

		if packtype != 4:
			#operator
			typeid = int(study[0])
			study = study[1:-1]+study[-1]

			if typeid == 0:
				#15bits
				payloadlength = hex2int(study[0:15])
				print("Len =", payloadlength)
				study = study[15:15+payloadlength]

				translation.append(study)
			else:
				pass
				#11bits
		else:
			binary = ''
			marker = 1
			while marker == 1:
				marker = int(study[0])
				section = study[1:5]
				study = study[5:-1]+study[-1]
				binary += section
			print("Found number:",hex2int(binary))

			if '1' in study:
				translation.append(study)

	print("The total sum of the packets is:", total)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))