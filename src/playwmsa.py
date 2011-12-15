#! /usr/bin/env python

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import AlignIO

def findIndels(seq):
    # Find all occurences of indels
    if seq.find('-') != -1:
        return True
    else:
        return False

    return pos

def checkAas(seq,rows):
    """ Checks if the sequences has more than 50% unique AA:s. """

    uniques = 0

    for i in range(rows):
        # If more than half are unique return True
        if uniques >= rows/2:
            return True

        # Check each aa
        char = seq[i]
        count = seq.count(char)
        if count == 1:
            uniques += 1
    
    return False

def buildSeqCols(alignment,rows, aas):
    """ Takes a multialignment, tansposes to columns and returns them. """

    multSeq = []

    for i in range(rows):
        multSeq += [list(alignment[i].seq)]

    # Transpose to cols
    multSeqCols = zip(*multSeq)
    
    return multSeqCols
    
def main():
    # Open the .phy-file from convert2phy.py
    path = '../data/outfile.phy'

    # Create handles for the files to be read and written to
    handle = open(path, 'r')
    
    # Parse the file
    alignment = AlignIO.read(handle, "phylip")

    # No of sequences
    rows = len(alignment)

    # No of aas
    aas = len(alignment[1].seq)

    # Transposes to cols
    multSeqCols = buildSeqCols(alignment, rows, aas)

    # Noise reduction step, for every residue position
    for i in range(aas-1, -1, -1):
        if findIndels(str(multSeqCols[i])) or checkAas(multSeqCols[i], rows):
            multSeqCols.pop(i)

    # Transpose back to sequence rows
    multSeq = zip(*multSeqCols)

    # Build output string in fasta format
    consensusStr = ''
    for i in range(rows):
        consensusStr += '>' + alignment[i].id + '\n' + ''.join(multSeq[i]) + '\n'

    # Create handle for the output file
    handleOut = open('../data/infile.fa', 'w')
    
    # Write to the output file in phylips format
    handleOut.write(consensusStr)

    # Close the handles
    handle.close()
    handleOut.close()

##    tempalignment = []
##    for c in range(aas):
##        tempCol = ''
##        for r in range(rows):
##
##            tempCol += alignment[r].seq[c]
##
##        if not findIndels(tempCol):
##            if not checkAas(tempCol, rows):
##                for i in range(rows):
##                    tempalignment += transpose(tempCol)
##                print tempCol
##        else:
##            print 'Removed'
            

if __name__ == '__main__':
    main()
