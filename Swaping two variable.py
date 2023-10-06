#first we will do with the help of the third variable i.e temp

x=13
y=12

temp=x
x=y

y=temp
print("Value of x",x)
print("Value of y",y)

#Now we will do it without third variable

x=13
y=12

x,y=y,x
print("Value of x",x)
print("value of y",y)
