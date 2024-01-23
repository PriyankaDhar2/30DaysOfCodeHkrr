S = input()
try:
    integer = int(S)
    print(integer)
except ValueError:
    print('Bad String')
