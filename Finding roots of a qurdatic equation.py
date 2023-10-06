#In this program we will first enter a quardtic equation then we will find the roots of the equation

#quardatic equation will look like this ax**2+bx+c=0
# a,b and c are the real numbers
# a!=0
#cmath is a library in the python which is used to solve the complex mathematics problem
import cmath

a= int(input("Enter the value of a"))
b= int(input("Enter the value of b"))
c= int(input("Enter the value of c"))

d= (b**2)-(4*a*c)

# d is the descriminant you learned in your mathematics

root1= -b-cmath.sqrt(d)
root2= -b+cmath.sqrt(d)

print("Root 1 is :",root1)
print("Root 2 is:",root2)
print ("The roots are",root1,"and",root2)

