"""
Problem Name: Bit++
Platform: Codeforces (282A)
Problem Link: https://codeforces.com/problemset/problem/282/A

Description:
Bit++ নামের একটি প্রোগ্রামিং ভাষায় শুধু একটি ভেরিয়েবল X আছে যার শুরুর মান 0।
দুটি অপারেশন করা যায়:
  - ++X বা X++ (X এর মান ১ বাড়ায়)
  - --X বা X-- (X এর মান ১ কমায়)
n-সংখ্যক এমন অপারেশন দেওয়া থাকলে X-এর চূড়ান্ত মান কত হবে?

ইনপুট: 
  - ১ম লাইনে মোট অপারেশনের সংখ্যা (n)।
  - পরবর্তী n-টি লাইনে অপারেশন (যেমন: ++X, X--)।
আউটপুট: X এর চূড়ান্ত মান।
"""
#সমাধান
a=int(input())
x=0
for i in range(a):
	statment=input()
	if "+" in statment:
		x += 1
	else:
			x -=1
print(x)
