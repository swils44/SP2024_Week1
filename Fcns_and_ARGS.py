# region functions
def trapezoidal(fcn, a, b, args=None, nPoints=100):
    """
    calculates the area under a function between limits of a and b
    :param fcn: A callback for the function in question
    :param a: The lower limit of the integration
    :param b: The upper limit of the integration
    :param args: optional arguments as a tuple
    :param nPoints: number of points for my integration
    :return: area under fcn between a and b
    """
    # step size along x axis
    stepsize = (b-a)/(nPoints - 1)

    #evaluate fcn(a)  with possibility of args
    if args is None:  fa = fcn(a)
    else: fa = fcn(a,args)
    sum = fa

    if args is None: fb = fcn(b)
    else:fb = fcn(b, args)
    sum += fb

    for i in range(1, nPoints - 1): #loop over all interior points
       xi = a + i * stepsize

       if args is None: fxi = fcn(xi)
       else: fxi = fcn(xi, args)

       sum += 2*fxi
    #next i
    return sum*stepsize/2

def f1(x,args):
    """
    This function takes a tuple of arguments called args, unpacks into a, b, c and calculates f(x)
    :param x: x value for evaluating f(x)
    :param args: a tuple containing scalars a, b, c
    :return: value of f(x)
    """
    a,b,c = args  # this is known as unpacking the arguments
    return a*x**2 + b*x + c

def f3(x):
    """
    A less versitle function with 'hard coded' coefficients for a, b, c
    :param x: x value for evaluating f(x)
    :return: value of f(x)
    """
    return 5*x**2 + 2*x + 4

def test_trap():
    """
    Actually executes the trapazoidal integration method for a function defined within this function.
    Recall, the trapazoidal method divides the x range into uniform steps of width h, calculates the area of the trapazoid
    defined by (x1, f(x1)) and (x2,f(x2)).
    :return: the area under the curve
    """
    def f2(x):
        """
        This is to be passed as a callback function to the trapazoidal function for evaluating f(x).
        :param x:
        :return: f(x):  that is the y value of the function at x
        """
        #move outside of test_trap later to see what happens
        return a*x**2 + b*x + c

    valf3_a = trapezoidal(f3, 0, 4, nPoints=20)
    print("f3 ",valf3_a)

    a = 1; b = 2; c = 3  # this makes its way into f2() because of scope of a, b, c & f2
    valf2_a = trapezoidal(f2, 0, 4, nPoints=20)
    print("f2a ",valf2_a)

    a = 3; b = 2; c = 1  # this makes its way into f2() because of scope of a, b, c & f2
    valf2_b = trapezoidal(f2, 0, 4, nPoints=20)
    print("f2b ",valf2_b)

    #now look at f1.  a, b, c are in different scope than f1, so pass as args
    valf1_a = trapezoidal(f1, 0, 4, args = (a,b,c), nPoints=20)
    #valf1_a = trapezoidal(f1, 0, 4,argsnpoints=20)
    print("f1 ",valf1_a)

    vallambda = trapezoidal(lambda x: a*x**2 + b*x + c, 0, 4)
    print("vallambda ",vallambda)

    b=5

    return vallambda

def main():
    """
    This function tests the trapezoidal method for integrating a function.  See numerical methods tutorial for details.
    :return:
    """
    myval = test_trap()
    print(myval)
# endregion

main()

