n = int(input("Enter a Number : "))

for i in range(1,n+1):
    #Left Bars
    print( ((2*n)-(2*i))*"-",end="" )
    
    #Left side Numbers
    for j in range(1,i+1):
        print(j,end="")
        #Bars between Numbers
        if( i!=1):
            print("-",end="")
    
    #Right side Numbers
    for k in range(i-1,0,-1):
        print(k,end="")
        #Bars between Numbers
        if( k!= 1 ):
            print("-",end="")
    
    #Right side Bars
    print( ((2*n)-(2*i))*"-" )

for i in range(1,n):
    print( (2*i)*"-",end="" )
    for j in range(n-i):
        print(j+1,end="")
        if( j!=n-i-1 ):
            print("-",end="")
    
    if( i!=n-1 ):
        print("-",end="")
        
    for k in range(n-i-1,0,-1):
        print(k,end="")
        if( k!=1):
            print("-",end="")
    
    print((2*i)*"-")
    
"""

Output:
--------1--------
------1-2-1------
----1-2-3-2-1----
--1-2-3-4-3-2-1--
1-2-3-4-5-4-3-2-1
--1-2-3-4-3-2-1--
----1-2-3-2-1----
------1-2-1------
--------1--------

"""