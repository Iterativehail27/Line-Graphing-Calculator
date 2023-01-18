import math
import matplotlib.pyplot as plt
x1 = float(input("Enter a x coordinate for x1: "))
y1 = float(input("Enter a y coordinate for y1: "))
x2 = float(input("Enter a x coordinate for x2: "))
y2 = float(input("Enter a y coordinate for y2: "))

try: m = (y2-y1)/(x2-x1)
except ZeroDivisionError:
    m = 0
d = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
slope_multiplied_by_negative_x1 = m * (-1 * x1)
b = float(y1) + float(slope_multiplied_by_negative_x1)
b_absolute = abs(b)
result = "y = " + (str(m) + "x " if m != 0 else "")

if m == 0:
    sign = ""
elif b == 0:
    sign = ""
elif b > 0:
    sign = "+ "
else:
    sign = "- "

try: X_intercept = float((-1 * b)/m)
except ZeroDivisionError:
    X_intercept = 'n/a'

y1y2 = str('Y intercept = ' + str(b))
x1x2 = str('X intercept = ' + str(x1))

if y1 == y2 and X_intercept == 'n/a':
    print('y = ' + str(y1))
else:
    print(result + sign + ("" if b == 0 else (str(b_absolute)))) if x1 != x2 else print(str('x = ' + str(x1)))
print("X intercept: " + ("0.0" if X_intercept == 0 else str(X_intercept))) if x1 != x2 else print(x1x2)
print("Y intercept: " + str(b)) if m != 0 else print("Y intercept: n/a") if y1 != y2 else print(y1y2)
print("Distance between (x1,y1) and (x2,y2): " + str(d))

fig, ax = plt.subplots()
plt.plot(0, 0, color='k', marker='')  # just to make sure the plot contains 0,0
if X_intercept != 'n/a':
    plt.plot([X_intercept, x1], [0, y1], color='m', marker='o', linewidth=0.5)
    plt.plot([X_intercept, x2], [0, y2], color='m', marker='', linewidth=0.5)
if b != 'n/a':
    plt.plot([0, x1], [b, y1], color='m', marker='o', linewidth=0.5)
    plt.plot([0, x2], [b, y2], color='m', marker='', linewidth=0.5)
plt.plot([x1, x2], [y1, y2], color='c', linestyle='-', marker='o')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid()
plt.show()
