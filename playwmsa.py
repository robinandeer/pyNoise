#! /usr/bin/env python

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import AlignIO
#from Bio.Align import MultipleSeqAlignment

def findIndels(seq):
    # Find all occurences of indels
    if seq.find('-') != -1:
        return True
    else:
        return False
    # Translate response to position indexes
    #pos = [(m.group(), m.start()) for m in pattern.finditer(seq)]

    return pos

def checkAas(seq,rows):
    """ Checks if the sequences has more than 50% unique AA:s. """

    uniques = 0

    for i in range(rows):
        if uniques >= rows/2:
            return True
        char = seq[i]
        count = seq.count(char)
        if count == 1:
            uniques += 1
    
    return False
    
def main():
    # Open the first file in the easy folder
    path = 'outfile.phy'

    # Create handles for the files to be read and written to
    handle = open(path, 'r')
    #handleOut = open('outfile2.phy', 'w')
    
    # Parse the file
    alignment = AlignIO.read(handle, "phylip")

    # No of sequences
    rows = len(alignment)

    # No of aas
    aas = len(alignment[1].seq)
    print aas

    tempalignment = []

##    for r in range(rows):
##        tempalignment += ['']
##    print tempalignment

    for c in range(aas):
        tempCol = ''
        for r in range(rows):

            tempCol += alignment[r].seq[c]

        if not findIndels(tempCol):
            if not checkAas(tempCol, rows):
                for i in range(rows):
                    tempalignment += transpose(tempCol)
                print tempCol
        else:
            print 'Removed'

            
        
    # Close the handles
    handle.close()

if __name__ == '__main__':
    main()
