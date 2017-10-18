#!/usr/bin/python

# http://rosalind.info/problems/edta/?class=437

str=""
str2=""
str=[]
with open('edta_input.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('>'):
            str.append('')
        else:
            str[-1] += line.strip()


str1 = str[0]
str2 = str[1]

dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
bt = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

#print dp
for i in range(1, len(str1)+1):
    dp[i][0] = i
for j in range(1, len(str2)+1):
    dp[0][j] = j
#print dp

#print len(dp)
#print len(dp[0])

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        #print i,j
        x = (str1[i - 1] != str2[j - 1])
        dp[i][j] = min(x + dp[i - 1][j - 1], 1 + dp[i - 1][j], 1 + dp[i][j - 1])
        if dp[i][j] == x + dp[i - 1][j - 1]:
            bt[i][j] = 0
        elif dp[i][j] == 1+dp[i-1][j]:
            bt[i][j] = 1
        else:
            bt[i][j] = 2

#for j in range(len(str2),-1,-1):
#    print dp[j]
#print bt
i = len(str1)
j = len(str2)
s1 = str1
s2 = str2
while i>0 and j>0:
    if bt[i][j] == 1:
        i -= 1
        s2 = s2[:j] + '-' + s2[j:]
    elif bt[i][j] == 2:
        j -= 1
        s1 = s1[:i] + '-' + s1[i:]
    else:
        i-=1
        j-=1

#print s1
#print s2
for _ in range(i):
    s2 = s2[:0] + '-' + s2[0:]
for _ in range(j):
    s1 = s1[:0] + '-' + s1[0:]

print dp[len(str1)][len(str2)]
print s1
print s2
