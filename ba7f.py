#!/usr/bin/python

#http://rosalind.info/problems/ba7f/?class=437

nuc = ['A', 'C', 'T', 'G']
leaves = []
nodes = {}

cost = 0
def print_tree(root):
    if not root:
        return
    print_tree(root.left)
    print root.id, root.full
    print_tree(root.right)

def hamming(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d

def hamming_tree_traversal(root):
    if not root:
        return
    if root.left:
        d = hamming(root.full, root.left.full)
        print root.full + '->' + root.left.full + ':' + str(d)
        print root.left.full + '->' + root.full + ':' + str(d)
    if root.right:
        d = hamming(root.full, root.right.full)
        print root.full + '->' + root.right.full + ':' + str(d)
        print root.right.full + '->' + root.full + ':' + str(d)

    hamming_tree_traversal(root.left)
    hamming_tree_traversal(root.right)

def pre(root):
    global cost
    if not root:
        return
    m1 = 999999999
    if not root.parent:
        for i in range(len(nuc)):
            if root.arr4[i] < m1:
                m1 = root.arr4[i]
                root.c = nuc[i]
        cost += m1
        root.full += root.c
    elif not root.leaf:
        m1 = 999999999
        for i in range(len(nuc)):
            c=1
            if nuc[i] == root.parent.c:
                c=0
            if c + root.arr4[i] < m1:
                m1 = c + root.arr4[i]
                root.c = nuc[i]
        root.full += root.c

    pre(root.left)
    pre(root.right)

def post(root):
    if not root:
        return
    post(root.left)
    post(root.right)
    if root.leaf:
        for i in range(len(nuc)):
            if root.c == nuc[i]:
                root.arr4[i] = 0
            else:
                root.arr4[i] = 999999999
    else:
        for i in range(len(nuc)):
            m1 = 999999999
            for j in range(len(nuc)):
                c=1
                if i == j:
                    c = 0
                m1 = min(m1, c + root.left.arr4[j])
            m2 = 999999999
            for j in range(len(nuc)):
                c=1
                if i == j:
                    c = 0
                m2= min(m2, c + root.right.arr4[j])

            root.arr4[i] = m1 + m2


class Node:
    def __init__(self, _id, leaf, full=''):
        self.c = None
        self.full = full
        self.arr4 = [0 for _ in range(4)]
        self.left = None
        self.right = None
        self.parent = None
        self.id = _id
        self.leaf = leaf


num_l = None
with open('ba7f_input.txt', 'r') as f:
    for line in f.readlines():
        read = line.strip()
        if not num_l:
            num_l = read
            continue
        fr, to = read.split('->')

        if fr not in nodes:
            fn = Node(fr, False)
            nodes[fr] = fn
        else:
            fn = nodes[fr]

        if to[0] in nuc:
            _id = 'l' + str(len(leaves))
            leaves.append(to)
            tn = Node(_id, True, to)
            nodes[_id] = tn
            if not fn.left:
                fn.left = tn
            else:
                fn.right = tn
            tn.parent = fn
        else:
            tn = nodes[to]
            if not fn.left:
                fn.left = tn
            else:
                fn.right = tn
            tn.parent = fn

#print leaves

for _id, node in nodes.iteritems():
    if not nodes[_id].parent and not nodes[_id].leaf:
        root = nodes[_id]
        break

for i in range(len(leaves[0])):
    for j in range(len(leaves)):
        _id = 'l' + str(j)
        nodes[_id].c = leaves[j][i]

    post(root)
    pre(root)

#print_tree(root)
print cost
hamming_tree_traversal(root)
