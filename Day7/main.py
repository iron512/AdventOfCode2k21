#!/usr/bin/env python3

import time

def factsum(n):
	total = 0
	for i in range(n+1):
		total += i
	return total

def main():
	data = [int(x) for x in open("input.txt","r").read().split(",")]
	#data = [16,1,2,0,4,2,7,1,2,14]
	costs = [0] * (max(data)+1)
	crabcost = [0] * (max(data)+1)
	crabfuel = [0] * (max(data)+1)

	for position in range(len(crabfuel)):
		crabfuel[position] = factsum(position)

	for position in range(len(costs)):
		for crab in data:
			costs[position] += abs(crab - position)
			crabcost[position] += crabfuel[abs(crab - position)]

	print("The least amount of fuel to spend is:",min(costs))
	print("The least amount of crab fuel to spend is:",min(crabcost))

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))