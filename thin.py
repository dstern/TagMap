#!/usr/bin/env python

import sys

file_to_thin = sys.argv

with open(file_to_thin[1]) as f:
	lines = f.read().splitlines()

num_lines = len(lines)

for x in list(reversed(range(1,num_lines))):
	first = lines[x-1].split('\t')
	second = lines[x].split('\t')
	if first[0] == second[0]:
		diff = int(second[1]) - int(first[1])
		if diff < 100:
			del lines[x]

with open (str(file_to_thin[1])+'.candidate_sites','w') as output:
	for y in lines:
		output.write(y+"\n")