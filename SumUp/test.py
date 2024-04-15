from SumUp import SumUp
import random

import time

t1= time.time()

results = {}
num_sums_list = []
num_unique_digits = []


for i in range(150):
    #create random 10-card hand.
    hand = random.choices(["0","1","2","3","4","5","6","7","8","9"], k=10)
    sums = SumUp(hand)
    num_sums = sums.max_sum_fast()
    print(hand, num_sums)
    num_sums_list.append(num_sums)
    num_unique_digits.append(len(set(hand)))

with open("num_hands_with_digits_10-card.csv", "w") as f:
    f.write("num_hands,num_unique_digits")
    f.write("\n")
    for i in range(len(num_sums_list)):
        f.write(str(num_sums_list[i])+","+str(num_unique_digits[i]))
        f.write("\n")

t2 = time.time()
total_time = t2 - t1
print(f"Elapsed Time: {total_time}")