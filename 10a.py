n = int(input("Enter a Number : "))
for i in range(1,n+1):
    print( (n-i)*" " + str(i)*i + str(i)*(i-1))
    
for i in range(1,n):
    print( i*" " + str(n-i)*(n-i) + str(n-i)*(n-(i+1)) )


"""

Output:
    1
   222
  33333
 4444444
555555555
 4444444
  33333
   222
    1

"""