#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n\n")
	#data = open("test.txt","r").read().split("\n\n")
	template, transitions = data

	transitions = transitions.split("\n")
	#print(template)

	tranMap = {}
	for rule in transitions:
		pair, product = rule.split(" -> ")
		tranMap[pair] = product

	steps = 10
	#steps = 4

	for i in range(steps):
		 #print(i, len(template))
		result = [template[0]]
		for j in range(len(template)-1):
			seek = template[j] + template[j+1]
			result.append(tranMap[seek])
			result.append(template[j+1])
		template = "".join(result)
		#print(template)

	elements = {}
	for letter in template:
		if letter not in elements:
			elements[letter] = 0
		elements[letter] += 1

	print(elements)
	values = [elements[index] for index in elements]
	print("The most-least subtraction is: ", max(values) - min(values))

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))