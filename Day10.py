n = int(input().strip())
binary_representation = bin(n)[2:]
consecutive_ones = 0
max_consecutive_ones = 0

for digit in binary_representation:
    if digit == '1':
        consecutive_ones += 1
        max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
    else:
        consecutive_ones = 0

print(max_consecutive_ones)


#binary conversion and count of consecutive 1s