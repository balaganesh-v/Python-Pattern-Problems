import math

n = int(input("Enter a Number : "))
for i in range(n):
    print( (n-i)*" ",end="")
    for j in range(i+1):
        print("-",end="")
    for k in range(1,i+1):
        print("-",end="")
    print()

m=math.ceil(n/2)

for i in range(n):
    print( math.ceil(n/2)*" " + n*"-" +(n+n)*" " + n*"-")

for i in range(m):
    print( math.ceil(n/2)*" "+ (n+n+n+n)*"-")
    
for i in range(n):
    print( math.ceil(n/2)*" " + n*"-" + (n+n)*" "+ n*"-")
    
for i in range(n):
    print( (3*n)*" " + (i+1)*" " + (n-i)*"-" + (n-(i+1))*"-")
    
    
"""

Output:
Enter a Number : 5
     -
    ---
   -----
  -------
 ---------
   -----          -----
   -----          -----
   -----          -----
   -----          -----
   -----          -----
   --------------------
   --------------------
   --------------------
   -----          -----
   -----          -----
   -----          -----
   -----          -----
   -----          -----
                ---------
                 -------
                  -----
                   ---
                    -

"""