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

def extractNextPacket(candidate):
	packets = []

	packet = candidate[0:6]
	candidate = candidate[6:-1]+candidate[-1]

	if hex2int(packet[3:6]) == 4:
		#literal
		marker = 1
		while marker == 1:
			marker = int(candidate[0])
			packet += candidate[0:5]
			candidate = candidate[5:-1] + candidate[-1]

		packets.append(packet)
	else:
		#operator
		if candidate[0] == '0':
			#15bits
			length = hex2int(candidate[1:16])
			packet += candidate[0:16+length]
			candidate = candidate[16:-1] + candidate[-1]

			packets.append(packet)

			insidecan = packet
			while '1' in insidecan:
				found, insidecan = extractNextPacket(insidecan)
		else:
			#11bits
			count = hex2int(candidate[1:12])
			packet += candidate[0:12]
			candidate = candidate[12:-1] + candidate[-1]

			newpack = []
			insidecan = candidate
			for i in range(count):
				found, insidecan = extractNextPacket(insidecan)
				newpack.append(found)

			for item in newpack:
				packet += item
				packets.append(item)
			packets.append(packet)

	return packets, candidate

def main():
	data = open("input.txt","r").read()
	data = open("test1.txt","r").read()
	data = open("test2.txt","r").read()
	data = open("test3.txt","r").read()
	data = "38006F45291200"

	translation = ""
	for char in data:
		translation += char2hex(char)

	packets, candidate = extractNextPacket(translation)
	print(packets)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))