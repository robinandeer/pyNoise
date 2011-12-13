#! /usr/bin/env python

import dendropy
path = '../data/asymmetric_0.5/asymmetric_0.5.tree'

# Set the same taxon_set for all trees!
taxa = dendropy.TaxonSet()

tree1 = dendropy.Tree.get_from_path(path, schema="newick", taxon_set=taxa)
tree2 = dendropy.Tree.get_from_path(path, schema="newick", taxon_set=taxa)
#treeObj = dendropy.Tree(stream=open(path), schema="newick")

tree_str = "(((sp5,sp4),(((((((((((sp14,sp1),sp13),sp12),sp9),sp8),sp10),sp11),sp15),sp7),sp16),sp6)),sp3,sp2);"

treeStr = dendropy.Tree.get_from_string(tree_str, schema="newick", taxon_set=taxa)
treeStr2 = dendropy.Tree.get_from_string(tree_str, schema="newick", taxon_set=taxa)

##print "Original:"
##print treeStr.as_ascii_plot()

##for i in range(5):
##    print treeStr.leaf_nodes()

# Compare the trees!
print dendropy.treecalc.robinson_foulds_distance(tree1, tree2)
