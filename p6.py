#!/usr/bin/python

# http://rosalind.info/problems/prob/?class=437

import math

dna_str = "TCAAGTTAAGTTGCTGAATTAACTGTTATGTCATCTTCTGGGATCAATCCGTAATTGTCGGGAGGGTATGTCCACTTAGACACGTGGCGTTCCCCTTT"
probabilities = [0.068, 0.175, 0.205, 0.311, 0.313, 0.386, 0.476, 0.548, 0.615, 0.665, 0.717, 0.763, 0.817, 0.909]
answers = []
for p in probabilities:
    gc = (p*1.0)/2.0
    ta = (1.0 - (p*1.0))/2.0
    ans = 1.0
    for dna in dna_str:
        if dna == 'G' or dna == 'C':
            ans *= gc
        elif dna == 'T' or dna == 'A':
            ans *= ta
    answers.append(math.log10(ans))

for ans in answers:
    print format(ans, '.3f'),