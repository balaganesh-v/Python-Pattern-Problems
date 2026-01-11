n = int(input("Enter a number : "))
for i in range(n):
    print( (n-i)*"-" + i*" " + (i)*" " + (n-i)*"-" )

for i in range(n):
    print( (i+1)*"-" + (n-i-1)*" " + (n-i-1)*" " + (i+1)*"-")
