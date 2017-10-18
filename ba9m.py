#!/usr/bin/python

# http://rosalind.info/problems/ba9l/?class=437

input_file = open('rosalind_ba9m.txt', 'r')

input = input_file.read()

l = len(input)

rpat = False
str = ""
word = ""
patterns = []
for i in range(0, l):
    c = input[i]
    if not rpat and c != " ":
        str += c
    else:
        if c != ' ':
            word += c
        else:
            patterns.append(word)
            word = ""
    if c == '\n':
        rpat = True

patterns.append(word)

#print str
#print patterns

freq = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}

rk = {
    'A': -1,
    'C': -1,
    'T': -1,
    'G': -1
}

for i in str:
    if i != '$' and i != '\n':
        freq[i] += 1

first = "$" + "A" * freq['A'] + "C" * freq['C'] + "G" * freq['G'] + "T" * freq['T']

rank = {}
for i in range(0, len(str)):
    c = str[i]
    if c != '$' and c != '\n' and rk[c] != -1:
        rank[i] = rk[c] + 1
        rk[c] = rank[i]
    else:
        rk[c] = 0
        rank[i] = 0

#print first

rowi = 0
t = '$'

while str[rowi] != '$':
    c = str[rowi]
    t = c+t
    pos = 1
    for key, val in freq.iteritems():
        if key < c:
            pos += val
    pos += rank[rowi]
    rowi = pos

#print t

for pat in patterns:
    print t.count(pat),