b, tk, m = map(int, input().split())

total_cost = 0

# ১ থেকে m পর্যন্ত লুপ ঘুরবে মোট দাম বের করার জন্য
for i in range(1, m + 1):
    total_cost += b * i  # প্রতিটা কলার দাম total_cost এর সাথে যোগ হচ্ছে

# লুপের বাইরে এসে একবার চেক করব ধার করা লাগবে কি না
if total_cost > tk:
    print(total_cost - tk)  # খরচ বেশি হলে কত টাকা ধার লাগবে
else:
    print(0)  # টাকা বেশি বা সমান থাকলে কোনো ধার লাগবে না (0 টাকা)
  
