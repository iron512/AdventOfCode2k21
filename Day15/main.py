#!/usr/bin/env python3

import time
import networkx as nx

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test.txt","r").read().split("\n")
	data = open("enhanced.txt","r").read().split("\n")

	xmax = len(data)
	ymax = len(data[0])

	G = nx.DiGraph()
	G.add_nodes_from(range(xmax*ymax))

	for x in range(xmax):
		for y in range(ymax):
			if x>0 and y>0:
				G.add_edge(x*xmax+y,x*xmax+(y-1))
				G.add_edge(x*xmax+y,(x-1)*xmax+y)
				
				G.add_edge(x*xmax+(y-1),x*xmax+y)
				G.add_edge((x-1)*xmax+y,x*xmax+y)

				G[x*xmax+y][x*xmax+(y-1)]["weight"] = int(data[x][y-1])
				G[x*xmax+y][(x-1)*xmax+y]["weight"] = int(data[x-1][y])

				G[x*xmax+(y-1)][x*xmax+y]["weight"] = int(data[x][y])
				G[(x-1)*xmax+y][x*xmax+y]["weight"] = int(data[x][y])

			elif y==0 and x>0:
				G.add_edge(x*xmax+y,(x-1)*xmax+y)
				G.add_edge((x-1)*xmax+y,x*xmax+y)

				G[x*xmax+y][(x-1)*xmax+y]["weight"] = int(data[x-1][y])
				G[(x-1)*xmax+y][x*xmax+y]["weight"] = int(data[x][y])

			elif x==0 and y>0:
				G.add_edge(x*xmax+y,x*xmax+(y-1))
				G.add_edge(x*xmax+(y-1),x*xmax+y)
				
				G[x*xmax+y][x*xmax+(y-1)]["weight"] = int(data[x][y-1])
				G[x*xmax+(y-1)][x*xmax+y]["weight"] = int(data[x][y])

	path = nx.shortest_path(G,0,(xmax-1)*xmax+ymax-1,"weight")

	total = -int(data[0][0])
	for node in path:
		y = node%ymax
		x = int(node/xmax)

		total += int(data[x][y])

	print(G[102])
	print("The lowest risk path is:",total)

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))