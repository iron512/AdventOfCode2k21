#!/usr/bin/env python3

import sys
import time

def main():
	data = open("input.txt","r").read().split("\n\n")
	#data = open("test.txt","r").read().split("\n\n")

	extraction  = data[0]
	data.remove(extraction)

	extraction = extraction.split(",")

	tables = []
	for elem in data:
		rows = elem.split("\n")
		group = []
		for row in rows:
			group.append(row.replace("  "," ").split(" "))
		tables.append(group)

	for group in tables:
		for row in group:
			if "" in row:
				row.remove("")

		columns = [[] for i in range(5)]
		for row in group:
			for j in range(len(row)):	
				columns[j].append(row[j])

		for column in columns:
			group.append(column)

	found = False
	index = 0
	toRmv = []
	while not found:
		val = extraction[index]
		index+=1
		
		for group in tables:
			for row in group:
				if val in row:
					row.remove(val)

			toRmv = group
			for row in group
				if sum([int(x) for x in row]) == 0:
					found = True

					total = 0
					for row in group:
						total += sum([int(x) for x in row])

					total/=2
					print("Winning board total sum:", int(total))
					print("Extraction number:", val)
					print("First product:",int(total)*int(val))
					break;

	tables.remove(toRmv)
	while len(tables) != 1:
		val = extraction[index]
		index+=1

		toRmv = []		
		for group in tables:
			for row in group:
				if val in row:
					row.remove(val)
			
			for row in group:
				if sum([int(x) for x in row]) == 0:
					found = True
					toRmv.append(group)

		for elem in toRmv:
			if elem in tables:
			tables.remove(elem)
	
	print()
	final = tables[0]
	found = False
	while not found:
		val = extraction[index]
		index+=1

		for row in final:
			if val in row:
				row.remove(val)

		for row in final:
			if sum([int(x) for x in row]) == 0:
				found = True

				total = 0
				for row in group:
					total += sum([int(x) for x in row])

				total/=2
				print("Losing board total sum:", int(total))
				print("Extraction number:", val)
				print("Last product:",int(total)*int(val))
				break;

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))