#!/usr/bin/python

#http://rosalind.info/problems/dbru/?class=437

kmers = set()

complement = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

def get_reverse_complement(read):
    str1 = ""
    for c in read:
        str1 = complement[c] + str1
    return str1

with open('dbru_input.txt', 'r') as f:
    for line in f.readlines():
        read = line.strip()
        l = len(read)
        kmers.add(read)
        kmers.add(get_reverse_complement(read))

#print kmers
adj_list = {}

for kmer in kmers:
    le, ri = kmer[0:l-1], kmer[-(l-1):]
    adj_list.setdefault(le, []).append(ri)

for key, val in adj_list.iteritems():
    for v in val:
        print "(" + key + ", " + v + ")"
