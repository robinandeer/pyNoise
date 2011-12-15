#! /usr/bin/env python

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import AlignIO

def main():

    # test if files exist
    try:
        file(sys.argv[1], 'r')
    except IOError:
        sys.stderr.write("The file '" + sys.argv[1] + "' doesn't exist.\n")
        sys.exit()

    handle = open(sys.argv[1],'r')
    
    # Create handles for the files to be read and written to
    handleOut = open('../data/outfile.phy', 'w')
    
    # Parse the file
    for record in AlignIO.parse(handle, "fasta"):

        # Write to the output file in phylips format
        handleOut.write(record.format('phylip'))

    # Close the handles
    handle.close()
    handleOut.close()
    
if __name__ == '__main__':
    main()
