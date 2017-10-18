#!/usr/bin/python

# http://rosalind.info/problems/splc/?class=437

codon_table = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'Stop',
    'UGG': 'W',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}

input_file = open('p3_input1.txt', 'r')

input = input_file.read()

dna_str = ""
intron = ""
introns = []

dna_chars = ['A', 'T', 'C', 'G']
interested_str = False
identifier_str = False
string_number = 0

l = len(input)
for i in range(l):
    c = input[i]
    if c == '>':
        string_number += 1
        identifier_str = True
        interested_str = False
    if c == ' ' or c == '\t' or c == '\n':
        if identifier_str:
            identifier_str = False
            interested_str = True
        elif interested_str:
            if string_number > 1:
                introns.append(intron)
                intron = ""
    if interested_str and c in dna_chars:
        if string_number == 1:
            dna_str = dna_str + c
        else:
            intron = intron + c

# add last intron
introns.append(intron)

for intron in introns:
    dna_str = dna_str.replace(intron, '')

new_dna_str = ""
l = len(dna_str)
for i in range(0, l):
    if dna_str[i] == 'T':
        new_dna_str += 'U'
    else:
        new_dna_str += dna_str[i]

protein_str = ""
for i in range(0, l, 3):
    condon = codon_table[new_dna_str[i:i+3]]
    if condon == 'Stop':
        break
    protein_str = protein_str + condon

print protein_str
