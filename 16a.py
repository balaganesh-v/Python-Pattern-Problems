n=int(input("Enter a Number : "))
for i in range(1,n+1):
    for j in range(i):
        print( chr(97+j),end="")
        if j<i-1:
            print("-",end="")
    print()

"""

Output:
a
a-b
a-b-c
a-b-c-d
a-b-c-d-e

"""