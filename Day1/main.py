#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")

	count = 0
	previous = int(data[0])
	for i in range(1,len(data)):
		if int(data[i]) > previous:
			count += 1
		previous = int(data[i])

	print("the count of depth increases is:", count)

	count = 0
	previous = int(data[0])
	for i in range(3,len(data)):
		if int(data[i]) > previous:
			count += 1
		previous = int(data[i-2])

	print("the count of precise depth increases is:", count)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))