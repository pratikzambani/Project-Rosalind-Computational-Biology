#!/usr/bin/python

# http://rosalind.info/problems/fibd/?class=437

n = 87
m = 20

dp=[1,1,1]

for i in range(3,n+1):
    if i-m-1 >= 0:
        dp.append(dp[i-1] + dp[i-2] - dp[i-m-1])
    else:
        dp.append(dp[i-1] + dp[i-2])

print dp[n]