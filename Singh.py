'''y=input("enter a value")
x=int(y)
print (x*1)
print (x*2)
print (x*3)
print (x*4)
print (x*5)
print (x*6)
print (x*7)
print (x*8)
print (x*9)
print (x*10)'''


'''print ("koter")'''
'''x=input ("write something")
x=int(x)
print (x*x*x)'''

'''lenth=input ("inter the lenth")
lenth=int(lenth)
width=input ("inter the width")
width=int(width)
print ("area is" , lenth*width)'''

'''redius=input("inter the redius")
redius=int(redius)
print ("circule area is", 3.4*redius*redius)'''

'''import math
string=input("inter a string")
a=len(string)
print (a)
string2=input("inter a string2")
b=len(string2)
print (b)
math.pow(a,b)
c=math.pow(a,b)
print (c)'''

'''import math
a=input ("inter a value")
a=int(a)
math.sqrt(a)
b=math.sqrt(a)
print(5==3)
print (round(b))'''

'''a=input ("inter a place")
if(a=="atarra"):
	print ("Turn Left")
elif(a=="banda"):
	print ("Turn right")
else:
	print ("invalid")
print ("done")'''

'''a,b=input("inter  number").split()
a=int(a)
b=int(b)
if(a%2==0):
	print (a+b)
else:
	print (a-b)'''

'''a,b=input("inter 2 numbers").split()
a=int(a)
b=int(b)
print ("use +for add, - for minus, * for multiple, \ for divide")
while (True):
	c=input ()

	if(c=="+"):
		print (a+b)
	elif(c=="-"):
		print (a-b)
	elif(c=="*"):
		print (a*b)
	elif(c=="/"):
		print (a/b)
	else:
		print ("inviled")'''
'''a=input ("input a number")
a=int(a)
if(a%2==0):
	print ("dividable from 2")
	if(a%3==0):	
		print ("dividable from 3")
	else:
		print ("not dividale from 3")
elif(a%3==0):	
	print ("dividable from 3")
	if (a%2!=0):
		print ("not dividable from 2")
else:
	print ("not dividable from 2 & 3")



if(a%2==0 && a%3=!=0):'''
'''
print ("Ajay Singh")
a,b=input ("inter 2 numbers").split()
a=int(a)
b=int(b)
if (a%2==0):
	print (a-b)
else:
	print (a+b)'''

'''for i in range(0,10):
	print (i*5+5)'''

#invrementing the values
'''s=0
s=s+1
s=s+5
s+=5'''
'''s=0
for a in range(1,101):
	s=s+a
	print(s,a)'''


'''a,b=input ("inter 2 number").split()
a=int(a)
b=int(b)
C=0
for s in range(a,b+1):
	C=C+s
	print(C)'''


''' factorial
a=input ("inter a number")
a=int(a)
s=1
for i in range(1,a+1):
	s=s*i
print(s)'''

'''for i in range (1,10+1):
	print (i)'''
'''print ("Ajay "*10)
x=input()
x=int(x)
for a in range (x):
	print ("* "*x)'''

'''for i in range (10, 100):
	print (100-i)'''

'''for i in range (2, 10):
	if (i%2==0):
		print (i)'''

'''a,b =input ("inter to number").split()
a=int(a)
b=int(b)
for i in range (a, b):
	if (i%2!=0):
		print (i)'''

'''odd & even number culculation
c=0
d=0
a,b =input ("inter to number").split()
a=int(a)
b=int(b)
for i in range (a, b):
	if (i%2==0):
		c=i+c
	else:
		d=i+d
print ("sum number totall-", (i+c))
print ("visum number totall-", (i+d))'''

c=0
d=0
a,b =input ("inter to number").split()
a=int(a)
b=int(b)
for i in range (a, b):
	if (i%2==0):
		c=c+i*i
		print (c)
