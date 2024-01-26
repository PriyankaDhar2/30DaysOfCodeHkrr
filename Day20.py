import math
import os
import random
import re
import sys

if __name__ == '__main__':
    def bubble_sort(arr):
        n = len(arr)
        total_swaps = 0

        for i in range(n):
            swaps_this_round = 0

            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps_this_round += 1

            total_swaps += swaps_this_round

            if swaps_this_round == 0:
                break

        return total_swaps, arr[0], arr[-1]


    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    swaps, first_element, last_element = bubble_sort(a)

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {first_element}")
    print(f"Last Element: {last_element}")

    
        

