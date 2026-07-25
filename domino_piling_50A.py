"""
Problem Name: Domino piling
Platform: Codeforces (50A)
Problem Link: https://codeforces.com/problemset/problem/50/A

Description:
M x N সাইজের একটি চারকোনা বোর্ডে ২ x ১ সাইজের ডমিনো বসাতে হবে। 
বোর্ডে সর্বোচ্চ কতটি ডমিনো বসানো সম্ভব?

ইনপুট: দুটি ইন্টিজার M এবং N।
আউটপুট: সর্বোচ্চ ডমিনোর সংখ্যা ((M * N) // 2)।
"""
m,n=map(int,input().split())

ghor=m*n

domino=ghor//2
print(domino)
