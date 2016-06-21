import sys
import getopt
import rpy2.robjects as robjects #for calling R agrepl
import subprocess #for calling R agrepl
from random import shuffle
import csv
import time

def main():
	time1=time.time()
        #parse command line options
        try:
                opts, arg = getopt.getopt(sys.argv[1:],"h", ["help"])
        except getopt.error, msg:
                print msg
                print "for help use --help"
                sys.exit(2)
        # process options
        for o, a in opts:
                if o in ("-h", "--help"):
                        print __doc__
                        sys.exit(0)
        if len(arg) < 3:
                print "Usage: python fuzzy_DNA_R.py <needle> <haystack.fq> <output file name> <Null_dist> <Score_only> <Max_score_to_keep (optional)> \n <Null_dist> and <Score_only> or True or False only."                
                sys.exit(0)
        #process arguments

	#define R objects
	agrepl = robjects.r['agrepl']

        afile= arg[0]
        bfile = arg[1]
        OutFile = arg[2]
	max_score_to_keep = 'False'
	
	if len(arg) > 2:
		null_dist = arg[3]
	else:
		null_dist = 'False'
	if len(arg) >3:
		score_only = arg[4]
	else:
		score_only = 'False'
		
	if len(arg) >4:
		max_score_to_keep = int(arg[5])
	else:
		max_score_to_keep = 'False'
		
        print "first file = %s" %(afile)
        print "second file = %s" %(bfile)
        print "Output File = %s" %(OutFile)
	print "Null distribution = %s" %(null_dist)
	print "Score only = %s" %(score_only)
	print "Max score to keep = %s" %(max_score_to_keep)
		
	f = open(afile)
	needle = f.readlines()
	needle = needle[0].strip()
	f.close()
	
	x=0
	y=0
	z=0
	match_value=[] 
	if score_only == 'False':
		fastq_name = [] 
		fastq_qual = [] 
		fastq_seq = [] 
		fastq_qualname = []
	with open(bfile) as all_haystacks:
		for idx,haystack in enumerate(all_haystacks):
			haystack=haystack.strip()
			if score_only == 'False':
				if y == 0:
					name=haystack
				if y == 1:					
					seq=haystack
				if y == 3:
					qual=haystack
			if y==1:
				if null_dist == 'True':
					haystack = shuffle_word(haystack)
				matchTF = agrepl(needle.upper(),haystack.upper(),max_score_to_keep)
			y+=1
			if y==4:
				y=0			
				if matchTF[0]:
					z+=1
					fastq_name.append(name)
					fastq_seq.append(seq)
					fastq_qual.append(qual)
					fastq_qualname.append('+')
			if idx % 100000 == 0:
				print idx,'sequences examined.',z,'matches'		
				time2=time.time()
				duration = time2-time1
				print duration, 'seconds'
				time1=time2				
	
	
	
	with open(OutFile, 'wt') as OF:
		out = csv.writer(OF, dialect='excel-tab')
		out.writerows(zip(fastq_name,fastq_seq,fastq_qualname,fastq_qual))
	OF.close()	

    
def shuffle_word(word):
	word=list(word)
	shuffle(word)
	return ''.join(word)

if __name__ == "__main__":
        sys.exit(main())


