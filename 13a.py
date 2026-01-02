n = int(input("Enter a Number : "))
for i in range(n):
    print( (n-i)*" ",end="")
    for j in range(i+1):
        print(chr(65+j ),end="")
    print()

"""

Output:
     A
    AB
   ABC
  ABCD
 ABCDE
 
"""