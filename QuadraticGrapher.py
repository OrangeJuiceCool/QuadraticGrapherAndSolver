import matplotlib.pyplot as plt
import math
import numpy as np

print("This is the Quadratic Grapher")
print("Before using, please install matplotlib")
print("A quadratic is written in the form ax^2+bx+c")
print("Please input your values for a, b and c when prompted")

a = float(input("Input your value for A."))
b = float(input("Input your value for b."))
c = float(input("Input your value for c."))

plt.grid(color='k', linestyle='-', linewidth=1)
# calculate delta and zero points
delta = b**2 - 4*a*c
if delta > 0:
    x_1 = (-b + math.sqrt(delta))/(2*a)
    x_2 = (-b - math.sqrt(delta))/(2*a)
if delta == 0:
    x_0 = -b/(2*a)
else:
    pass

# calculate parabola extreme coordinates
p = -b/(2*a)
q = -delta/(4*a)
extreme = [p,q]

# define parabola function
def parabola(x,a,b,c):
    y = a*x**2 + b*x + c
    return y

# plot function
x = np.linspace(int(p)-5,int(p)+5,100)
y = parabola(x,a,b,c)
plt.plot(x,y)
plt.axhline(y=0, color='black', linestyle='-', linewidth=3)
plt.axvline(x=0, color='black', linestyle='-', linewidth=3)
plt.text(p-0.5, q-3, '[' + str(round(p,2)) +',' + str(round(q,2)) + ']',color='red', fontsize=10)
plt.plot(p, q, marker="o", color = 'red')

if delta > 0:
    plt.plot(x_1, 0, marker="o", color='green')
    plt.text(x_1 - 0.5, 2, '[' + str(round(x_1,2)) + ']', color='green', fontsize=10)
    plt.plot(x_2, 0, marker="o", color='green')
    plt.text(x_2 - 0.5, 2, '[' + str(round(x_2,2)) + ']', color='green', fontsize=10)

if delta == 0:
    plt.plot(x_0, 0, marker="o", color='green')
    plt.text(x_0 - 0.5, 2, '[' + str(round(x_0,2)) + ']', color='green', fontsize=10)


plt.show()
