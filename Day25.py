def is_prime(n):
    if n <= 1:
        return "Not prime"
    elif n == 2:
        return "Prime"
    elif n % 2 == 0:
        return "Not prime"
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return "Not prime"
        return "Prime"

# Read the number of test cases
t = int(input().strip())

for _ in range(t):
    # Read the number to be tested for primality
    num = int(input().strip())
    
    # Check and print whether the number is prime or not
    result = is_prime(num)
    print(result)
