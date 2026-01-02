n=int(input("Enter a Number : "))
for i in range(n):
    print( (i+1)*" ",end="")
    for j in range(n-i):
        print( chr(65+j),end="")
    print()

"""

Output:
ABCDE
 ABCD
  ABC
   AB
    A
    
"""