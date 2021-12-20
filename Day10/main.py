#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")
	#data = ["<{([{{}}[<[[[<>{}]]]>[]]"]

	corruptedMap = {}
	corruptedVal = {")":3,"]":57,"}":1197,">":25137}
	incomplete = []

	for row in data:
		original = row
		changes = True
		while changes and len(row) > 0:
			changes = False
			if "()" in row or "[]" in row or "{}" in row or "<>" in row:
				changes = True
			row = row.replace("()","").replace("{}","").replace("[]","").replace("<>","")

		if len(row) != 0:
			#corrupted or incomplete
			corrupted = False
			for letter in row:
				if not corrupted and letter in [")","]","}",">"]:
					corrupted = True 
					if letter not in corruptedMap:
						corruptedMap[letter] = 0
					corruptedMap[letter] += 1
			
			if not corrupted:
				incomplete.append(row)

	total = 0
	for letter in corruptedMap:
		total += corruptedMap[letter] * corruptedVal[letter]
	print("The total score is:",total)

	scores = []
	marks = {"(":1,"[":2,"{":3,"<":4}
	
	for line in incomplete:
		line = line[::-1]
		total = 0
		for letter in line:
			total *= 5
			total += marks[letter]
		scores.append(total)
	scores = sorted(scores)
	print("The final incomplete score is:",scores[int(len(scores)/2)])

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))