#!/usr/bin/python
collection = {}
complement = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

with open('input.txt', 'r') as f:
    for l in f.readlines():
        if line.startswith('>'):
            continue
        else:
            r = l.strip()
            if r in collection.keys():
                comp = ""
                for c in r:
                    comp = complement[c] + str1
                collection[read] = comp
            else:
                collection[read] = 1

for key, val in collection.iteritems():
    if collection[key] == 1:
        str1 = ""
        for c in key:
            str1 = complement[c] + str1
        if str1 in collection:
            collection[key] = str1
            collection[str1] = key

#print collection

for key, val in collection.iteritems():
    if val == 1:
        for key1, val1 in collection.iteritems():
            if val1 == 1:
                continue
            cnt = 0
            for k in range(len(key)):
                if key[k] != key1[k]:
                    cnt += 1
            if cnt == 1:
                print key + "->" + key1
                break

            cnt = 0
            for k in range(len(key)):
                if key[k] != val1[k]:
                    cnt += 1
            if cnt == 1:
                print key + "->" + val1
                break
