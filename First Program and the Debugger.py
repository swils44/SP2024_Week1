import math
from math import tan
a = 5  # create a variable called a and assign it a value of 5
a += 1  # use the increment operator to increase the value of a by 1
a += 5  # use the increment operator to increase a by 5
b = 7.3  # create another variable called b and assign it a value of 7.3
c = a + b  # create another variable called c and assign it the value of a+b
d = c == 2 * a  # create another variable called d and assign it the result of the compare operator
D = 2 * a  # create another variable called D and assign it the value two times a
e = D == 2 * a
w = c / a  # create a variable called w and assign it the result of the divide operation
x = c // a  # use the floor division operator
y = round(c / a)  # use rounding to get the next highest integer
r = c % a  # use fmod from math module to find the remainder of the division c/a
R = r / a
print(math.tan(D))
print(tan(D))
print(f"R = {R:0.3f}")
print("tan(D) = {:0.3f}".format(tan(D)))
