#!/usr/bin/env python3

import time

def main():
	data = open("input.txt","r").read().split("\n")

if __name__ == '__main__':
	start = time.time()
	print()
	main()
	print()
	print("--- %s seconds ---" % (time.time() - start))