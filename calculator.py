#simple calculator using function
def add(*args):
	y=0
	for x in args:
		y=y+x
		print(y)

def multiply(*args):
	y=1
	for x in args:
		y=y*x
		print(y)

def subtract(x,y):
	print(x-y)
	

def divide(x,y):
	print(x/y)

#simple calculator without using function for two numbers
print('''what do you want to do????
	     1.add)
	     2.subtract
	     3.multiply
	     4.divide''')
a=int(input('choose your option'))
if a==1:
	x=int(input("enter the first number"))
	y=int(input("enter the second number"))
	print(x+y)
elif a==2:
	x=int(input("enter the first number"))
	y=int(input("enter the second number"))
	print(x-y)
elif a==3:
	x=int(input("enter the first number"))
	y=int(input("enter the second number"))
	print(x*y)
elif a==4:
	x=int(input("enter the first number"))
	y=int(input("enter the second number"))
	print(x/y)
else:
	print('you have only four option!!!')