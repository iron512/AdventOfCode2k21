#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")
	output = open("enhanced.txt","w")

	multiplier = 5


	enhanced = [[] for x in range(len(data))]

	for time in range(multiplier):
		for row in range(len(data)):
			for element in data[row]:
				candidate = int(element)+1*time
				if candidate > 9:
					candidate -= 9
				enhanced[row].append(candidate)

	for time in range(multiplier-1):
		for row in range(len(data)):
			enhanced.append([])
			for element in enhanced[row]:
				candidate = element + 1*(time+1)
				if candidate > 9:
					candidate -= 9
				enhanced[(time+1)*len(data)+row].append(candidate)

	for row in enhanced:
		for element in row:
			output.write(str(element))
		output.write("\n")
	print("Terminated and written to enhanced.txt")
	output.close()

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))