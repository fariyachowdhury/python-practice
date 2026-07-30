"""
Problem Name: Petya and Strings
Platform: Codeforces (112A)
Problem Link: https://codeforces.com/problemset/problem/112/A

Description:
পেত্যাকে দুটি সমদৈর্ঘ্যের শব্দ (String) দেওয়া হয়েছে। 
তাকে বলতে হবে লেক্সিকোগ্রাফিক্যালি (Lexicographically / অভিধানের বর্ণানুক্রমিক অর্ডার অনুযায়ী) 
কোন শব্দটি ছোট বা বড়।

শর্ত:
১. তুলনা করার সময় বড় হাতের বা ছোট হাতের অক্ষর (Case-insensitive) আলাদা ধরা যাবে না। 
   অর্থাৎ 'a' এবং 'A' কে সমান ধরতে হবে।
২. প্রথম শব্দ ছোট হলে আউটপুট: -1
৩. দ্বিতীয় শব্দ ছোট হলে আউটপুট: 1
৪. দুটি শব্দই সমান হলে আউটপুট: 0

ইনপুট:
- ১ম লাইনে ১ম শব্দ।
- ২য় লাইনে ২য় শব্দ।

আউটপুট:
- -1, 1, অথবা 0
"""

# সমাধান

a = input().lower()
b = input().lower()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
  
