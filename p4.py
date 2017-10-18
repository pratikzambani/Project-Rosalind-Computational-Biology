#!/usr/bin/python

# http://rosalind.info/problems/long/?class=437

def overlap(str1, str2):

    l1 = len(str1)
    l2 = len(str2)

    if str2 in str1:
        return str1

    minl = min(l1, l2)
    for ll in range(minl, (minl/2), -1):
        if str2[0:ll] == str1[-ll:]:
            return str1 + str2[ll:]

    for ll in range(minl, (minl/2), -1):
        if str1[0:ll] == str2[-ll:]:
            return str2 + str1[ll:]

    return ""

input_file = open('p4_input5.txt', 'r')

input = input_file.read()


dna_list = []
identifier = False
identifier_name = ""
identifier_dna = ""
l = len(input)

for i in range(0, l):
    c = input[i]
    if c == '>':
        if identifier_name and identifier_dna:
            dna_list.append(identifier_dna)
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

dna_list.append(identifier_dna)
#print dna_list
# for dna in dna_list:
#     print dna
l = len(dna_list)
print l
print dna_list[0]
print dna_list[l-1]
mergedstr = ""
bflag = False
for i in range(0, l):
    if bflag:
        break
    for j in range(i+1, l):
        mergedstr = overlap(dna_list[i], dna_list[j])
        if mergedstr:
            xx = dna_list[i]
            yy = dna_list[j]
            dna_list.remove(xx)
            dna_list.remove(yy)
            bflag=True
            break

#print 'initial merged ', mergedstr

str = ""
while len(dna_list):

    bflag = False
    for i in range(0, len(dna_list)):
        if bflag:
            break
        #print 'checking overlap of ', mergedstr, dna_list[i]
        str = overlap(mergedstr, dna_list[i])
        if str:
            mergedstr = str
            #print 'new merged str is ', mergedstr
            xx = dna_list[i]
            dna_list.remove(xx)
            bflag = True

#print mergedstr