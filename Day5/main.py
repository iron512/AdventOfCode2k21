#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")
	
	maxx = 1000
	maxy = 1000

	coordinatesSimp = {}
	coordinatesHard = {}
	countSimp = 0
	countHard = 0

	for row in data:
		x1, y1 = tuple([int(x) for x in row.split(" -> ")[0].split(",")])
		x2, y2 = tuple([int(x) for x in row.split(" -> ")[1].split(",")])

		if x1 == x2 or y1 == y2:
			for x in range(min(x1,x2), max(x1,x2)+1):
				for y in range(min(y1,y2), max(y1,y2)+1):
					if (x,y) not in coordinatesSimp:
						coordinatesSimp[(x,y)] = 0
					if (x,y) not in coordinatesHard:
						coordinatesHard[(x,y)] = 0		
					coordinatesSimp[(x,y)] += 1
					coordinatesHard[(x,y)] += 1
		else:
			#diagonal
			xin = 1
			if x1 > x2:
				xin = -1
			yin = 1
			if y1 > y2:
				yin = -1

			x = x1
			y = y1

			while x != x2+xin:
				if (x,y) not in coordinatesHard:
					coordinatesHard[(x,y)] = 0
				coordinatesHard[(x,y)] += 1
				y+=yin
				x+=xin


	for y in range(maxy):
		for x in range(maxx):
			if (x,y) in coordinatesSimp:
				if coordinatesSimp[(x,y)] > 1:
					countSimp += 1

	for y in range(maxy):
		for x in range(maxx):
			if (x,y) in coordinatesHard:
				print(coordinatesHard[(x,y)],end="")
				if coordinatesHard[(x,y)] > 1:
					countHard += 1
			else:
				print(".",end="")
		print()


	print("The count of simple overlaps is:", countSimp)
	print("The count of hard overlaps is:", countHard)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))