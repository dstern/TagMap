#!/bin/bash

# Filter out low-read hits

mkdir low_reads

cutoff=$1

for filename in *tview.txt; do
	nrows=(`wc ${filename} | tr -s ' ' | cut -d ' ' -f 2`)
	value=`expr $nrows - 2`
	if [ "$value" -gt "$cutoff" ]; then #|| (grep -q ' ttaa' $filename) || (grep -q 'TTAA ' $filename); then
		:
	else
		file_root=`echo $filename | cut -d'.' -f1`
		mv ${file_root}.* low_reads
	fi
done
