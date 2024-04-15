from itertools import permutations, combinations_with_replacement
import pandas as pd


class SumUp:
    def __init__(self, hand):
        self.hand = hand
        
    def max_sum_naive(self):

        hand = self.hand
        hand.extend(["+","=","b"])
        results = set()
        for seq in permutations(hand):
            if 0 < seq.index("+") < seq.index("=")-1 < seq.index("b")-2:
                #print(seq)
                i1, i2, i3 = seq.index("+"), seq.index("="), seq.index("b")
                num1 = int("".join(seq[:i1]))
                num2 = int("".join(seq[i1+1:i2]))
                num3 = int("".join(seq[i2+1:i3]))
                if num1 + num2 == num3:
                    results.add((num1,num2,num3))
        for item in results:
            print(item)

    def max_sum_fast(self):

        hand = self.hand

        #get all three-combinations that add to length of numbers in hand.
        # n = len(hand)
        # n_list = [i for i in range(1,n+1)]
        # sum_combs = list(combinations_with_replacement(n_list, 3))
        # digit_partitions = []
        # for element in sum_combs:
        #     if (sum(element) <= n) & (element[0]<=element[1]) & (element[1] == element[2] or element[1] == element[2]-1):
        #         digit_partitions.append(element)
        # with open("partitions.txt", "w") as f:
        #     for item in digit_partitions:
        #         f.write(f"{item}")

        digit_partitions = [(1,1,1),(1,1,2),(1,2,2),(1,2,3),(1,3,3),(1,3,4),(1,4,4),(1,4,5),(2,2,2),(2,2,3),(2,3,3),(2,3,4),(2,4,4),(3,3,3),(3,3,4)]
        # first_num = []
        # second_num = []
        third_num = []
        for trial in list(permutations(hand)):

            for element in digit_partitions:

                num_digits_first = element[0]
                num_digits_second = element[1]
                num_digits_third = element[2]

                i1 = num_digits_first
                i2 = num_digits_first+num_digits_second
                i3 = num_digits_first+num_digits_second+num_digits_third

                num1 = int("".join(trial[:i1]))
                num2 = int("".join(trial[i1:i2]))
                num3 = int("".join(trial[i2:i3]))

                if num1 + num2 == num3:
                    #first_num.append(num1)
                    #second_num.append(num2)
                    third_num.append(num3)
        return len(set(third_num))
        #print dataframe with all unique hands and sums, with max sum at the top.
        # df = pd.DataFrame({"num1":first_num, "num2":second_num, "sum_val":third_num})
        # df.drop_duplicates(inplace=True)
        # print(df.info())
        # df.sort_values(by=['sum_val'], axis=0, ascending=False, inplace=True)
        # max_sum = df["sum_val"].max()
        # unique_maxes = len(df[df["sum_val"] == max_sum])
        # print(df["sum_val"].nunique())
        # print(unique_maxes)
        # print(df.head(20))

        
        
    