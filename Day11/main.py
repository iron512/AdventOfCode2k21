#!/usr/bin/env python3

import time
import copy

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")

	parsed = []
	flashedBase = []
	total = 0
	
	parsed.append([-1 for x in range(len(data[0])+2)])
	for row in data:
		row = list(row)
		row.insert(0,'-1')
		row.append('-1')
		parsed.append([int(x) for x in row])
		flashedBase.append([False for x in range(len(data[0]))])

	parsed.append([-1 for x in range(len(data[0])+2)])

	for x in range(len(data)):
		for y in range(len(data[0])):
			xpos = x+1
			ypos = y+1
			print(parsed[xpos][ypos],end="")
		print()

	step = 100
	for z in range(step):
		flashed = copy.deepcopy(flashedBase)
		for x in range(len(data)):
			for y in range(len(data[0])):
				xpos = x+1
				ypos = y+1

				parsed[xpos][ypos] += 1

		changed = True
		while changed:
			changed = False
			for x in range(len(data)):
				for y in range(len(data[0])):
					xpos = x+1
					ypos = y+1

					if parsed[xpos][ypos] > 9 and not flashed[x][y]:
						flashed[x][y] = True
						changed = True

						parsed[xpos][ypos] -= 1
						for i in range(xpos-1,xpos+2):
							for j in range(ypos-1,ypos+2):
								if parsed[i][j] != -1:
									parsed[i][j] += 1

		for x in range(len(data)):
			for y in range(len(data[0])):
				xpos = x+1
				ypos = y+1

				if parsed[xpos][ypos] > 9:
					total += 1
					parsed[xpos][ypos] = 0
	print()
	for x in range(len(data)):
		for y in range(len(data[0])):
			xpos = x+1
			ypos = y+1
			print(parsed[xpos][ypos],end="")
		print()

	while sum([sum(row) for row in parsed]) != -44:
		step += 1
		flashed = copy.deepcopy(flashedBase)
		for x in range(len(data)):
			for y in range(len(data[0])):
				xpos = x+1
				ypos = y+1

				parsed[xpos][ypos] += 1

		changed = True
		while changed:
			changed = False
			for x in range(len(data)):
				for y in range(len(data[0])):
					xpos = x+1
					ypos = y+1

					if parsed[xpos][ypos] > 9 and not flashed[x][y]:
						flashed[x][y] = True
						changed = True

						parsed[xpos][ypos] -= 1
						for i in range(xpos-1,xpos+2):
							for j in range(ypos-1,ypos+2):
								if parsed[i][j] != -1:
									parsed[i][j] += 1

		for x in range(len(data)):
			for y in range(len(data[0])):
				xpos = x+1
				ypos = y+1

				if parsed[xpos][ypos] > 9:
					total += 1
					parsed[xpos][ypos] = 0
	print()
	for x in range(len(data)):
		for y in range(len(data[0])):
			xpos = x+1
			ypos = y+1
			print(parsed[xpos][ypos],end="")
		print()
	print()

	print("The number of flashes after 100 steps is:",total)
	print("The number steps for total flashes is:",step)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))