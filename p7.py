#!/usr/bin/python

# http://rosalind.info/problems/grph/?class=437

input_file = open('p7_input1.txt', 'r')

input = input_file.read()

identifier_map = {}
identifier = False
identifier_name = ""
identifier_dna = ""
l = len(input)

for i in range(0, l):
    c = input[i]
    if c == '>':
        if identifier_name and identifier_dna:
            identifier_map[identifier_name] = identifier_dna
        identifier = True
        identifier_name = ""
        identifier_dna = ""
    elif c != ' ' and c != '\t' and c != '\n':
        if identifier:
            identifier_name += c
        else:
            identifier_dna += c
    else:
        identifier = False

identifier_map[identifier_name] = identifier_dna

#print identifier_map
adj_list = []

for key in identifier_map:
    for key2, val2 in identifier_map.iteritems():
        if identifier_map[key] == identifier_map[key2]:
            continue
        #print 'comparing ', key, identifier_map[key][-3:],' with ', key2, val2[0:3]
        if identifier_map[key][-3:] == val2[0:3]:
            adj_list.append((key, key2))

for edge in adj_list:
    print edge[0], edge[1]
