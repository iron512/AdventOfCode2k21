#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	
	Hpos = 0
	Vpos = 0

	updatedHpos = 0
	updatedVpos = 0
	aim = 0

	for command in data:
		divided = command.split(" ")
		if divided[0] == "forward":
			Hpos += int(divided[1])
			updatedHpos += int(divided[1])
			updatedVpos += int(divided[1])*aim
		elif divided[0] == "up":
			Vpos -= int(divided[1])
			if Vpos < 0:
				Vpos = 0
			aim -= int(divided[1])
		elif divided[0] == "down":
			Vpos += int(divided[1])
			aim += int(divided[1])
		else: 
			print("wtf")

	print("The final positions are H:",Hpos," and V:",Vpos)
	print("The product is", Hpos*Vpos)
	print()
	print("The updated final positions are H:",updatedHpos," and V:",updatedVpos)
	print("The product is", updatedHpos*updatedVpos)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))