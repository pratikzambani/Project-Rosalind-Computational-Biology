#!/usr/bin/python

#http://rosalind.info/problems/ba3g/?class=437

adj_list = {}

with open('ba3g_input.txt', 'r') as f:
    for line in f.readlines():
        read = line.strip()
        fr, to = read.split(' -> ')
        tos = to.split(',')
        for t in tos:
            adj_list.setdefault(int(fr), []).append(int(t))

outminusin = {key : 0 for key in adj_list}

for key, val in adj_list.iteritems():
    outminusin[key] += len(val)
    for v in val:
        if v not in outminusin:
            outminusin[v] = 0
        outminusin[v] -= 1
#print outminusin

for v in outminusin:
    if outminusin[v] == 1:
        start = v
        break

node = start
st = [start]
ans = []
while len(st):
    if adj_list.get(node):
        new_node = adj_list[node][0]
        st.append(new_node)
        del adj_list[node][0]
        node = new_node
    else:
        ans.append(st.pop())
        if len(st):
            node = st[-1]

ansstr = str(ans[-1])
for i in range(len(ans)-2, -1, -1):
    ansstr +=  ("->" + str(ans[i]))

print ansstr
