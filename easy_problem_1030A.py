"""
Problem Name: In Search of an Easy Problem
Platform: Codeforces (1030A)
Problem Link: https://codeforces.com/problemset/problem/1030/A

Description:
n-সংখ্যক মানুষের ইনপুট নেওয়া হবে। 
যদি অন্তত একজন মানুষও 1 বলে (কঠিন মনে করে), তবে আউটপুট HARD।
আর সবাই যদি 0 বলে, তবে আউটপুট EASY।
"""

n = int(input())  # প্রথম লাইনের ইনপুট (মানুষের সংখ্যা)
a = list(map(int, input().split()))  # দ্বিতীয় লাইনের ০ ও ১-এর লিস্ট

if 1 in a:
    print("HARD")
else:
    print("EASY")
  
