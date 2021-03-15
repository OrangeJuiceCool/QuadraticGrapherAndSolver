from fractions import Fraction
import math

print("This is the Quadratic Formula Solver")
print("Please input your values for a, b and c when prompted")
print("A quadratic is written in the form ax^2+bx+c")


 
d = input("Input your value for A.")
e = input("Input your value for b.")
f = input("Input your value for c.")

inside = int(float(e))*int(float(e)) - 4*int(float(d))*int(float(f))

bottom = 2*int(float(d))    
if inside < 0:
	
	inside == Fraction(inside).limit_denominator()
	bottom == Fraction(bottom)
	print("Your answer has imaginary numbers. The solution for you quadratic (not-simplified) is: [-" + str(e) + " + or - i*sqrt(" + str(-1*inside) + ")]/["+str(bottom)+"] You will have to simplify this yourself on a piece of paper")

else:
	top1 = 1*int(float(e)) + math.sqrt(inside)
	top2 = 1*int(float(e)) - math.sqrt(inside)

	answer1 = top1/bottom
	answer2 = top2/bottom 

	answer1 = Fraction(answer1)
	answer2 = Fraction(answer2) 

	print("The solutions for your quadratic are: " + str(answer1.limit_denominator()) + " and " + str(answer2.limit_denominator()))

