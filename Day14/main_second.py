#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n\n")
	#data = open("test.txt","r").read().split("\n\n")
	template, transitions = data

	production = {}
	for j in range(len(template)-1):
		pair = template[j] + template[j+1]
		if pair not in production:
			production[pair] = 0
		production[pair] += 1

	print(template)
	print(production)

	transitions = transitions.split("\n")
	#print(template)

	tranMap = {}
	for rule in transitions:
		pair, product = rule.split(" -> ")
		tranMap[pair] = product

	steps = 40
	#steps = 4

	for step in range(steps):
		result = {} 
		for pair in production:
			new = tranMap[pair]
			first = pair[0] + new
			second = new + pair[1]

			if first not in result:
				result[first] = 0
			if second not in result:
				result[second] = 0

			result[first] += production[pair] 
			result[second] += production[pair]
		
		production = result

	elements = {}
	for pair in production:
		if pair[0] not in elements:
			elements[pair[0]] = 0
		if pair[1] not in elements:
			elements[pair[1]] = 0
		
		elements[pair[0]] += production[pair]
		elements[pair[1]] += production[pair]

	values = [int((elements[index]-1)/2+1) for index in elements]
	print("The most-least subtraction is: ", max(values) - min(values))


if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))