#! /usr/bin/env python

import sys, re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import AlignIO
#from Bio.Align import MultipleSeqAlignment

def findIndels(seq):
    # Find all occurences of indels
    pattern = re.compile('\-')
    # Translate response to position indexes
    pos = [(m.group(), m.start()) for m in pttrn.finditer(s)]

    return pos

def main():
    # Open the first file in the easy folder
    path = 'outfile.phy'

    # Create handles for the files to be read and written to
    handle = open(path, 'r')
    #handleOut = open('outfile2.phy', 'w')
    
    #alignments = []

    # Parse the file
    alignment = AlignIO.read(handle, "phylip")
    print "Number of rows: %i" % len(alignment)

    # RETURNS ERROR! TypeError: Row and Column indexing is not currently supported,but may be in future.
    # ON THE WEB IT SAYS YOU CAN DO IT, OLD VERSION?
    #print alignment[6]

    for record in alignment:
        seq = record.seq
        pos = findIndels(seq)
        
    # Close the handles
    handle.close()

if __name__ == '__main__':
    main()
