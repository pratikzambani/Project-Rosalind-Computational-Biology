#!/usr/bin/python

#http://rosalind.info/problems/pcov/?class=437

kmers = []

def check(ans, kmers):
    #print 'checking for ans', ans
    ans = ans * 2
    for kmer in kmers:
        if not kmer in ans:
            return False
    return True

with open('pcov_input.txt', 'r') as f:
    for line in f.readlines():
        kmer = line.strip()
        kmers.append(kmer)

l = len(kmers[0])
ans = kmers[0]

#print kmers

while not check(ans, kmers):
    le,ri = ans[:l-1], ans[-(l-1):]
    #print le, ri
    re = None
    for kmer in kmers:
        if ans == kmer:
            continue
        if le in kmer and kmer.endswith(le):
            ans = kmer[0] + ans
            re = kmer
            #print 'matched remove val', re
            break
        elif ri in kmer and kmer.startswith(ri):
            ans += kmer[-1]
            re = kmer
            #print 'matched remove val', re
            break
    if re:
        kmers.remove(re)

print ans
