#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")
	#data = ["2199943210","3987894921","9856789892","8767896789","9899965678"]
	xmax = len(data)
	ymax = len(data[0])

	for x in range(xmax):
		data[x] = '9' + data[x] +'9'

	data.insert(0,"".join(['9' for x in range(ymax+2)]))
	data.append("".join(['9' for x in range(ymax+2)]))


	minset = []
	basin = []
	for x in range(xmax):
		for y in range(ymax):
			posx = x+1
			posy = y+1
			sample = data[posx][posy] 

			if sample < data[posx+1][posy] and sample < data[posx-1][posy] and sample < data[posx][posy-1] and sample < data[posx][posy+1]:   
				print("\033[91m"+str(sample)+"\033[0m",end="")
				minset.append((posx,posy))
			else:
				print(sample,end="")
		print()
	
	total = 0
	for (x,y) in minset:
		total += int(data[x][y])+1
	print("The number of min points is:",total)	

	for (x,y) in minset:
		final = [(x,y)]
		probe = [(x,y)]

		while len(probe) != 0:
			tx,ty = probe.pop(0)
			if int(data[tx][ty]) < int(data[tx+1][ty]) and int(data[tx+1][ty]) != 9:
				if (tx+1,ty) not in final:
					final.append((tx+1,ty))
					probe.append((tx+1,ty))
			if int(data[tx][ty]) < int(data[tx-1][ty]) and int(data[tx-1][ty]) != 9:
				if (tx-1,ty) not in final:
					final.append((tx-1,ty))
					probe.append((tx-1,ty))
			if int(data[tx][ty]) < int(data[tx][ty+1]) and int(data[tx][ty+1]) != 9:
				if (tx,ty+1) not in final:
					final.append((tx,ty+1))
					probe.append((tx,ty+1))
			if int(data[tx][ty]) < int(data[tx][ty-1]) and int(data[tx][ty-1]) != 9:
				if (tx,ty-1) not in final:
					final.append((tx,ty-1))
					probe.append((tx,ty-1))
		basin.append(final)
	
	basinlen = []
	for element in basin:
		basinlen.append(len(element))
		#print(element)
	basinlen = sorted(basinlen)[::-1]


	if False:
		for element in basin:
			for x in range(xmax):
				for y in range(ymax):
					posx = x+1
					posy = y+1

					if(posx,posy) in element:
						print("\033[91m"+str(data[posx][posy])+"\033[0m",end="")
					else:
						print(str(data[posx][posy]),end="")
				print()
			print()
	if True:
		for x in range(xmax):
			for y in range(ymax):
				bas = False
				for element in basin:
					posx = x+1
					posy = y+1

					if(posx,posy) in element:
						bas = True
				
				if bas:
					print("\033[91m"+str(data[posx][posy])+"\033[0m",end="")
				else:
					print(str(data[posx][posy]),end="")
			print()

	print(basinlen)
	print("The final product of basins is :", basinlen[0]* basinlen[1]* basinlen[2])


if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))