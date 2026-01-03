n = int(input("Enter a Number : "))
for i in range(1,n+1):
    #Left side bars
    print( ((2*n)-(2*i))*"-",end="" )
    
    #Left side Letters and bars
    for j in range(i):
        print( chr(97+(n-(j+1))),end="" )
        if(j != i-1):
            print("-",end="")
    
    #Middle bars
    if(i>1):
        print("-",end="")
    
    #Right side letters and bars
    for k in range(i-2,-1,-1):
        print( chr( 97 + (n-(k+1)) ),end="" )
        if(k != 0):
            print("-",end="" )
            
    #Right side bars
    print( ((2*n)-(2*i))*"-" )

for i in range(1,n):
    #Left side bars
    print( (2*i)*"-",end="" )
    
    #Left side letters and bars
    for j in range(n-i):
        print( chr(97+(n-(j+1))),end="")
        if( j!= n-i-1):#It prints until end of the range in loop
            print("-",end="")

    #Middle bars
    if( i != n-1 ):
        print("-",end="")
    
    #Right side letters and bars
    for k in range(n-i-1):
        print( chr(97+(k+i+1)),end="" )
        if( k!= n-i-2):
            print("-",end="")
    
    #Right side bars
    print( (2*i)*"-")


"""

Input:
5

Excepted Output :
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Output Got:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
