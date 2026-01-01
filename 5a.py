n = int(input("Enter a Number : "))

for i in range(n):
    print( (n-i)*" " + (i+1)*"*" + i*"*" )
    
for i in range(n):
    print( (i+2)*" " + (n-(i+1))*"*" + (n-(i+2))*"*" )


"""

Output:
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *


"""