x = 6
y = 1000

print("x = " , x , "y = " , y)

print ("x == y", x == y)
print ("x != y", x != y)
print ("x <= y", x <= y)
print ("x >= y", x >= y)
print ("x < y", x < y)
print ("x > y", x > y)

print("x == 6 and y==1000", (x==6) and (y==1000) )
print("x == 6 and y==100", (x==6) and (y==100) )

print("x == 6 or y==6", (x==6) or (y==6) )
print("x == 7 or y==7", (x==7) or (y==7) )

print("not(x == y)", not(x == y) )

if ( x < 7 ):
	print("x < 7")
else:
	print("x >= 7" )


print("Enter number")

number = input()

if ( int(number) > 7 ):
	print("Your number is greater than 7")
else:
	        print("Your number is smaller than or equal to 7")


