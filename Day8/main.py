#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")
	#data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

	count = 0
	for row in data:
		section = row.split(" | ")[1].split(" ")
		for digit in section:
			if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
				count+=1

	print("The amount of 1, 4, 7 or 8 in the displays is:", count)

	#part2
	dioporco = 0
	for row in data:
		section = []
		section = [sorted(x) for x in row.split(" | ")[0].split(" ")]
		display = [sorted(x) for x in row.split(" | ")[1].split(" ")]
		
		pos1 = -1
		pos3 = -1
		pos4 = -1
		pos7 = -1
		pos8 = -1

		for i in range(len(section)):
			if len(section[i]) == 2:
				pos1 = i
			if len(section[i]) == 3:
				pos7 = i
			if len(section[i]) == 4:
				pos4 = i
			if len(section[i]) == 7:
				pos8 = i
		
		for i in range(len(section)):
			if len(section[i]) == 5 and len(set(section[pos1]).intersection(set(section[i]))) == 2:
				pos3 = i

		digits = [0 for x in range(4)]

		for i in range(len(display)):
			segment = display[i]
			#easy pass
			if len(segment) == 2:
				digits[i] = '1'
			if len(segment) == 3:
				digits[i] = '7'
			if len(segment) == 4:
				digits[i] = '4'
			if len(segment) == 7:
				digits[i] = '8'

			#hardpass
			if len(segment) == 6:
				#0/6/9
				if len(set(section[pos3]).intersection(set(segment))) == 5:
					digits[i] = '9'
				else:
					if len(set("".join(section[pos1])).intersection(set("".join(segment)))) == 2:
						digits[i] = '0'
					else:
						digits[i] = '6'

			if len(segment) == 5:
				#2/3/5
				if segment == section[pos3]:
					digits[i] = '3'
				else:
					#2/5
					#print(segment, section[pos3], pos3)

					a = set(section[pos4])
					b = set(segment)
					total = a.intersection(b)
					if len(total) == 3:
						digits[i] = '5'
					else:
						digits[i] = '2'
		dioporco += int("".join(digits)) 
	print("The total sum of the digits is:", dioporco)


if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))