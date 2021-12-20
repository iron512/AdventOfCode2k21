#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n\n")
	#data = open("test.txt","r").read().split("\n\n")
	toprint = True
	toprint = False

	dots, folds = data
	dots = dots.split("\n")
	folds = folds.split("\n")

	xmax = 0
	ymax = 0

	for pair in dots:
		x,y = pair.split(",")

		xmax = max(int(x)+1,xmax)
		ymax = max(int(y)+1,ymax)

	sheet = []
	for y in range(ymax):
		sheet.append([])
		for x in range(xmax):
			sheet[y].append(0)

	for pair in dots:
		x,y = pair.split(",")
		x = int(x)
		y = int(y)

		sheet[y][x] = 1

	#print
	if toprint:
		for y in range(len(sheet)):
			for x in range(len(sheet[0])):
				print("." if sheet[y][x] == 0 else "#",end="")
			print()

	first = True
	#folds = [folds[0]]
	for fold in folds:
		fold = fold.replace("fold along ","")
		axis, position = fold.split("=")
		position = int(position)

		if axis == "y":
			for i in range(min(position, len(sheet)-position-1)+1):
				for j in range(len(sheet[0])):
					sheet[position-i][j] += sheet[position+i][j]
			
			while len(sheet) != position:
				sheet.pop()
		else:
			for i in range(len(sheet)):
				for j in range(min(position, len(sheet[0])-position-1)+1):
					sheet[i][position-j] += sheet[i][position+j]

			while len(sheet[0]) != position:
				for row in sheet:
					row.pop()

		#print
		if toprint:
			print()
			for y in range(len(sheet)):
				for x in range(len(sheet[0])):
					print("." if sheet[y][x] == 0 else "#",end="")
				print()

		if first:
			first = False
			count = 0
			for i in range(len(sheet)):
				for j in range(len(sheet[0])):
					if sheet[i][j] != 0:
						count+=1
			print("After the first fold the visible dots are:",count)

	count = 0
	for i in range(len(sheet)):
		for j in range(len(sheet[0])):
			if sheet[i][j] != 0:
				count+=1
	print("In the end, the visible dots are:",count)

	print()
	for y in range(len(sheet)):
		for x in range(len(sheet[0])):
			print(" " if sheet[y][x] == 0 else "\u2588",end="")
		print()

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))