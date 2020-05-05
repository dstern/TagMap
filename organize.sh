#!/bin/bash

# place files from same individual in folder

for filename in *fastq.gz; do
	strain=`echo $filename | cut -d'.' -f1`
	mkdir $strain
	mv ${strain}.* $strain
done


