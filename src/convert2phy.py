#! /usr/bin/env python
##import dendropy
##path = 'appbio11/asymmetric_0.5/asymmetric_0.5.tree'
##
##tree1 = dendropy.Tree.get_from_path(path, schema="newick")
##treeObj = dendropy.Tree(stream=open(path), schema="newick")
##
##tree_str = "[&R] (A, (B, (C, (D, E))));"
##
##print "Original:"
##print tree1.as_ascii_plot()

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import AlignIO
#from Bio.Align import MultipleSeqAlignment

def main():

    # test if files exist
    try:
        file(sys.argv[1], 'r')
    except IOError:
        sys.stderr.write("The file '" + sys.argv[1] + "' doesn't exist.\n")
        sys.exit()

    handle = open(sys.argv[1],'r')
    
    # Open the first file in the easy folder
    #path = '../data/asymmetric_0.5/s001.align.1.msl'

    # Create handles for the files to be read and written to
    #handle = open(path, 'r')
    handleOut = open('../data/outfile.phy', 'w')
    
    #alignments = []

    # Parse the file
    for record in AlignIO.parse(handle, "fasta"):
        #alignments.append(record)

        # Write to the output file in phylips format
        handleOut.write(record.format('phylip'))

    # Close the handles
    handle.close()
    handleOut.close()
    
if __name__ == '__main__':
    main()
