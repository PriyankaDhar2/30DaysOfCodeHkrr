N = int(input().strip())
if (N%2==0):
    if N>20:
        print("Not Weird")
    elif N==20 or 20>N>6:
        print("Weird")
    elif 5>N>2:
        print("Not Weird")
else:
    print("Weird")
            
