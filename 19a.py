n = int(input("Enter a Number : "))

for i in range(n):
    print( i*"-",end="" )
    for j in range(i,n):
        print( chr(65+j),end="" )
    for k in range(1,n-i):
        print( chr(65+(n-k-1)),end="" )
    print( i*"-" )
    
for i in range(1,n):
    print( (n-i-1)*"-",end="")
    for j in range(1,i+2):
        print( chr(65+(n-i+j-2)),end="" )
    for k in range(1,i+1):
        print( chr(65+(n-k-1)),end="" )
    print( (n-i-1)*"-" )


"""
Output:
ABCDEFGHIJIHGFEDCBA
-BCDEFGHIJIHGFEDCB-
--CDEFGHIJIHGFEDC--
---DEFGHIJIHGFED---
----EFGHIJIHGFE----
-----FGHIJIHGF-----
------GHIJIHG------
-------HIJIH-------
--------IJI--------
---------J---------
--------IJI--------
-------HIJIH-------
------GHIJIHG------
-----FGHIJIHGF-----
----EFGHIJIHGFE----
---DEFGHIJIHGFED---
--CDEFGHIJIHGFEDC--
-BCDEFGHIJIHGFEDCB-
ABCDEFGHIJIHGFEDCBA

"""