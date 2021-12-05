#!/usr/bin/env python3

import time
import copy

def main():
	data = open("input.txt","r").read().split("\n")
	#data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

	count = [0] * len(data[0])

	for i in range(len(data)):
		for j in range(len(data[0])):
			count[j] += int(data[i][j])

	#print(count)
	gamma = ["0"]*len(data[0])
	epsilon = ["0"]*len(data[0])

	gammaVal = 0
	epsilonVal = 0

	for j in range(len(data[0])):
		if count[j] > len(data)/2:
			gamma[j] = "1"
			gammaVal += pow(2,len(data[0])-1-j)

		else:
			epsilon[j] = "1"
			epsilonVal += pow(2,len(data[0])-1-j)


	print("Gamma","".join(gamma),"-",gammaVal)
	print("Epsilon","".join(epsilon),"-",epsilonVal)
	print("Product:", gammaVal*epsilonVal)
	print()

	CO2 = copy.copy(data)
	O2 = copy.copy(data)

	for j in range(len(O2[0])):
		if len(O2) != 1:
			count = 0
			for i in range(len(O2)):
				count += int(O2[i][j])
				result = "1"
				if count >= (len(O2)/2):
					result = "0"

			toRmv = []
			for i in range(len(O2)):
				if O2[i][j] == result:
					toRmv.append(O2[i])

			for elem in toRmv:
				O2.remove(elem)

	value = O2[0]
	decimalOx = 0
	for j in range(len(value)):
		decimalOx += int(value[j]) * pow(2,len(value)-1-j)

	print("Oxygen",value,"-", decimalOx)

	for j in range(len(CO2[0])):
		if len(CO2) != 1:
			count = 0
			for i in range(len(CO2)):
				count += int(CO2[i][j])
				result = "1"
				if count < len(CO2)/2:
					result = "0"

			toRmv = []
			for i in range(len(CO2)):
				if CO2[i][j] == result:
					toRmv.append(CO2[i])

			for elem in toRmv:
				CO2.remove(elem)

	value = CO2[0]
	decimalCo = 0
	for j in range(len(value)):
		decimalCo += int(value[j]) * pow(2,len(value)-1-j)

	print("Carbon dioxide",CO2[0],"-",decimalCo)
	print("Product:", decimalCo*decimalOx)



if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))