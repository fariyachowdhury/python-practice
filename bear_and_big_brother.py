"""
Problem Name: Bear and Big Brother
Platform: Codeforces (791A)
Problem Link: https://codeforces.com/problemset/problem/791/A

Description:
ভালুক লিমাক (ওজন a) আর তার বড় ভাই বব (ওজন b)। লিমাকের ওজন প্রতি বছর ৩ গুণ হয় (a * 3) 
এবং ববের ওজন প্রতি বছর ২ গুণ হয় (b * 2)। 
কয় বছর পর লিমাকের ওজন ববের ওজনের চেয়ে কঠোরভাবে বেশি (a > b) হবে?

ইনপুট: দুটি ইন্টিজার a এবং b।
আউটপুট: মোট কত বছর লাগবে সেই সংখ্যা।
"""
#সমাধান
a,b=map(int,input().split())
year=0
while a<=b:
	a=a*3
	b=b*2
	year+=1
print(year)
