#!/bin/sh

#
# Evaluating the merits of a simple noise reducing algorithm for multiple 
# sequence alignments. One folder at a time.
#

# Fix no such file error
# http://www.gizmola.com/blog/archives/87-Linux-shell-scripting-bad-interpreter-No-such-file-or-directory.html

# Progress initiator
count=0

# Remove file with distances because we append
rm ../results/distances.txt

# Loop over all .msl in the specified folder
for f in ../data/symmetric_0.5/*.msl
do
	# Output	
	clear
	echo $count/300
	count=`expr $count + 1`

	# Converts msl to phy
	python convert2phy.py $f
	
	# Noise reducing algorithm, outputs .fa	
	python playwmsa.py
	
	# Calculates distance matrix and fnj makes a tree in newick format
	fastprot ../data/infile.fa | fnj -O 'newick' -o '../data/treeout.txt'

	# Compares result to refTree and outputs to results file, two cols. 
	python cmpTrees.py reduced

	# Same but no noise reduced tree
	fastprot ../data/outfile.phy -I 'phylip' | fnj -O 'newick' -o '../data/treeout.txt'
	python cmpTrees.py normal

done


