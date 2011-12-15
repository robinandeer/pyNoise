#! /usr/bin/env python

import dendropy
import sys

def main():
    # Paths to reference and current tree to be compared
    pathRef = '../data/asymmetric_0.5/asymmetric_0.5.tree'
    pathCal = '../data/treeout.txt'

    # Set the same taxon_set for all trees!
    taxa = dendropy.TaxonSet()

    refTree = dendropy.Tree.get_from_path(pathRef, schema="newick", taxon_set=taxa)
    calTree = dendropy.Tree.get_from_path(pathCal, schema="newick", taxon_set=taxa)
    
    # Open result-file
    handle = open('../results/distances.txt', 'a')

    # Compare the trees and append to file, differentiates noise reduced and normal trees
    if sys.argv[1] == 'reduced':
        handle.write(str(dendropy.treecalc.robinson_foulds_distance(calTree, refTree)) + '\t')
    else:
        handle.write(str(dendropy.treecalc.robinson_foulds_distance(calTree, refTree)) + '\n')
    
    handle.close

if __name__ == '__main__':
    main()
