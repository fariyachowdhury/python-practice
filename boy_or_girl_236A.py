"""
Problem Name: Boy or Girl
Platform: Codeforces (236A)
Problem Link: https://codeforces.com/problemset/problem/236/A

Description:
একজন ইউজার বয় নাকি গার্ল তা তার ইউজারনেম দিয়ে নির্ধারণ করতে হবে।
নিয়ম হলো: 
ইউজারনেমে থাকা **অনন্য/আলাদা (distinct) অক্ষরের সংখ্যা** যদি জোড় (Even) হয়, 
তবে সে মেয়ে (CHAT WITH HER!)।
আর যদি ইউনিক অক্ষরের সংখ্যা বিজোড় (Odd) হয়, 
তবে সে ছেলে (IGNORE HIM!)।

ইনপুট:
- এক লাইনে একটি ইউজারনেম (String, যেমন: "wシアm" বা "xiaodaba")।

আউটপুট:
- জোড় হলে: "CHAT WITH HER!"
- বিজোড় হলে: "IGNORE HIM!"
"""

#shomadhan


s = input()
letters = set(s)
b = len(letters)

if b % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
