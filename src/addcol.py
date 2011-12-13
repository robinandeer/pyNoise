rows = [line.split('\t') for line in file('tabdelim.dat')]
print rows
cols = zip(*rows) # transposes 2Dlist
print cols
cols.insert(2, ['Hunter', 'Sierig', 'Hunter', 'Hunter'])
rows = zip(*cols) # transpose back
print rows
#file('newfile.dat', 'w').writelines(['\t'.join(row) for row in rows])
