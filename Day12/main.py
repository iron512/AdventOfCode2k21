#!/usr/bin/env python3

import time
import copy

paths = []
pathstwice = []
path = []
count = []

def DFStwice(G,v):
	if v == "end":
		path.append("end")
		tmp = copy.deepcopy(path)
		pathstwice.append(tmp)
		path.pop()
	else:	
		path.append(v)
		for w in G[v]:
			if w != "start":
				if w.islower() and w != "end":
					found = False
					for k in path:
						if k.islower() and path.count(k) > 1:
							found = True

					if not found or w not in path:
						DFStwice(G,w)
				else:
					DFStwice(G,w)
		path.pop()

def DFS(G,v):
	if v == "end":
		path.append("end")
		tmp = copy.deepcopy(path)
		paths.append(tmp)
		path.pop()
	else:	
		path.append(v)
		for w in G[v]:
			if not w.islower() or path.count(w) < 1:
				DFS(G,w)
		path.pop()

def main():
	data = open("input.txt","r").read().split("\n")
	#data = open("test3.txt","r").read().split("\n")
	#data = open("test2.txt","r").read().split("\n")
	#data = open("test1.txt","r").read().split("\n")

	cave = {"start":[],"end":[]}

	for row in data:
		entrance, exit = row.split("-")

		if entrance not in cave:
			cave[entrance] = []
		if exit not in cave:
			cave[exit] = []

		cave[entrance].append(exit)
		cave[exit].append(entrance)

	DFS(cave,"start")
	path = []
	DFStwice(cave,"start")

	for path in pathstwice:
		print(path)

	print("The number of possible paths is:", len(paths))
	print("The number of possible paths, twice visiting all the small caves is:", len(pathstwice))

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))