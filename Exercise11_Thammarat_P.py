number = int(input())
for x in range(number):
    print(" " * (number-(x-1)) + "*" * ((x+1)+x))

#" " * 1 - (0-1) + "*" * (0+1)+0
#" " * 2 - (1-1) + "*" * (1+1)+1
#" " * 3 - (2-1) + "*" * (2+1)+2