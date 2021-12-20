#!/usr/bin/env python3

import time

def main():
	data = [int(x) for x in open("input.txt","r").read().split(",")]
	#data = [3,4,3,1,2]

	days = 256
	fishes = [0]*9
	print(fishes)

	for fish in data:
		fishes[fish] += 1

	print(fishes)
	for day in range(days):
		for i in range(len(fishes)):
			if i == 0:
				spawn = fishes[0]
			else:
				fishes[i-1] = fishes[i]
		fishes[6] += spawn
		fishes[8] = spawn
		
		#print(fishes)
		if day+1 == 18:
			print("The school of lanternfish after",day+1,"is composed by",sum(fishes),"lanternfish.")
		if day+1 == 80:
			print("The school of lanternfish after",day+1,"is composed by",sum(fishes),"lanternfish.")
	print("The school of lanternfish after",days,"is composed by",sum(fishes),"lanternfish.")

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))