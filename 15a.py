n = int(input("Enter a Number : "))
for i in range(n):
    print( (n-i)*" ",end="")
    for j in range(i+1):
        print(chr(65+i-j),end="")
    for k in range(i):
        print(chr(65+(k+1)),end="")
    print()
    
for i in range(1,n+1):
    print(i*" ",end=" ")
    for j in range(1,(n-i)+1):
        print( chr(65+(n-(i+j))),end="" )
    for k in range(1,n-i):
        print( chr(65+k),end="" )
    print()

"""

Output:
     A
    BAB
   CBABC
  DCBABCD
 EDCBABCDE
  DCBABCD
   CBABC
    BAB
     A
     
"""