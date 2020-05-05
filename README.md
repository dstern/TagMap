# TagMap
The shell script pBac_tagmap_0.2.sh can be used to analyze the data resulting from TagMap sequencing.
See 

https://www.biorxiv.org/content/10.1101/037762v5 

for a description of the method.


Install all the dependencies, as listed in the shell script. Place all of the *.fastq.gz files together with the shell script, thin.py, and the target genome sequence in one folder and run the shell script as follows

> ./pBac_tagmap_0.2.sh <target_genome.fa>

You will see two kinds of results files.

<sample_name.fq>.chromosome.bp.gnuplot.ps
<sample_name.fq>.chromosome.bp.tview.txt

There may be multiple results for each sample, which is preliminary evidence that the line contains multiple inserts.

Open the *gnuplot.ps plot and it should have red (forward reads) and blue (reverse reads) dots. There will also either be red or blue crosses, these indicate reads that overlap the transposable element end, and therefore indicate the orientation of the insertion. Red crosses indicate the insertion is in forward orientation, blue is reverse (according to the transposable element ends that you provide in the shell script).

Note that the base pair position indicated in the file name is approximate!!! You will need to determine the precise insertion by examining the *tview.txt file (see below). However, it is pretty easy to sort the file names and quickly identify multiple lines with the same approximate insertion site (within ~20-30 bp). These are almost always repeats of the same insertion.

If you are using non-piggyBac transposable elements, you need to change lines 37 and 38 of the shell script.

In the *tview.txt file you will see a pileup of reads “near” the target insertion site. Forward reads are in capital letters, reverse reads in lowercase letters. They should overlap at the insertion site (TTAA). 

For reasons I haven’t yet figured out, the “target” can drift a bit depending on the genome used. In any case, you can tune this by changing the number on line 131. So, for example from the default 

start=`expr "$insert_bp" - 35`

to 

start=`expr "$insert_bp" - 50`


Please reach out to me at sternd@hhmi.org if you have any questions. I am well aware that this is an outline of instructions! I hope to take more time to provide a more detailed description.
