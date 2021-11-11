import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# A program to compute the integral of a function numerically, using a range of methods (which
# includes the Trapezoidal Rule, Simpson's Rule and the Scipy.integrate subpackage.)
# Author: Zane Ali
    
# The analytic result of the definite integral of y = exp(-x)*sin(x) with limits 0 and 2:
result = 0.46662966259317557
 
# -------------------------------------------------------------------------------------------------
# Defining the Integrand
# -------------------------------------------------------------------------------------------------

# The function to be integrated.
def myFunction(x):
    f = float(np.exp(-x)*np.sin(x)) 
    return f

# Obtains x and y values for a function f with n points over a user-defined
# range [xmin, xmax]. 
def plotFunction(f, n, xmin, xmax):
    xlist = []
    ylist = []
    xmin = 0;
    xmax = np.pi;
    xlist = np.linspace(xmin, xmax, n);
    for x in xlist:
        ylist.append(f(x))
   
    plt.plot(xlist, ylist);
    plt.ylabel('f(x) = exp(-x)sin(x)')
    plt.xlabel('x')
    plt.title('Numerical Integrand')
    plt.savefig('Function.jpg', dpi = 300)
   

# -------------------------------------------------------------------------------------------------
# Using the Trapezium Rule 
# -------------------------------------------------------------------------------------------------

# Used to approximate the definite integral of myFunction between the limits a and b 
# via the Trapezium rule (with n strips)
def TrapeziumRule(a, b, n):
    h = float(b - a) / n
    y0 = myFunction(a)
    yn = myFunction(b)
    ysum = 0.0
   
    for x in range(n-1):
        ysum = ysum + myFunction(a + h*(x+1));
        
    total = (y0 + yn + 2*(ysum))*(h/2)
    return total
    
# Creates a table showing the values of the approximations for myFunction using TrapeziumRule
# with different values for the number of strips, n. 
def TrapeziumRuleTable(a, b):
    f = open("TrapeziumRuleTable.txt","w")

    f.write("A table of approximations for the integral of the function provided to" +
            " numericalintegration.py which\n have been calculated by the trapezium rule," +
            " where n is the number of trapezia. " + "\n\n" +
          "" + "n" + "\t\t" + "Integral Approximation" +"\n" +
          str(1) + "\t\t" + str(TrapeziumRule(a, b, 1)) + "\n" + 
          str(10) + "\t\t" + str(TrapeziumRule(a, b, 10)) + "\n" + 
          str(100) + "\t\t" + str(TrapeziumRule(a, b, 100)) + "\n" +
          str(1000) + "\t\t" + str(TrapeziumRule(a, b, 1000)) +"\n" +
          str(10000) + "\t\t" + str(TrapeziumRule(a, b, 10000)) + "\n" +
          str(100000) + "\t\t" + str(TrapeziumRule(a, b, 100000)))
    
    
 # Produces a log_10-log_10  scatter plot of the relative error (for approximations using the 
 # trapezium rule) against the number of strips n.
 # The number of data points, i, must be specified.
 # Note: Values of i > 6 will require a substantial waiting time for the program to produce 
 # an output. Additionally, values of i < 2 will fail to produce a line of best fit.
def TrapeziumErrorPlot(a, b, i):
     i+=1
     xValues = []
     yValues = []
     x = 1
    
     while x < i:
        yValues.append(np.log10(np.abs((TrapeziumRule(a, b, pow(10, x-1))/result) - 1)))
        xValues.append(x-1)
        x+=1
    
     fig = plt.figure()
     a, b = best_fit(xValues, yValues)
     plt.scatter(xValues, yValues)
     yfit = [a + b * xi for xi in xValues]
     
     
     plt.plot(xValues, yfit)
     fig.suptitle('Trapezoidal Rule: Relative Error\ny = {:.2f} + {:.2f}x'.format(a, b), fontsize=10)
     plt.xlabel('log(n)', fontsize=12)
     plt.ylabel('log(Error)', fontsize=12)
     plt.savefig('TrapeziumErrorPlot.jpg', dpi = 300)

     

# -------------------------------------------------------------------------------------------------
# Using Simpson's Rule 
# -------------------------------------------------------------------------------------------------

# Used to approximate the definite integral of myFunction between the limits a and b 
# via the composite Simpson's Rule (with n strips). 
def SimpsonsRule(a, b, n):
    
    h = float(b - a) / n
    
    sumEven = 0.0
    sumOdd = 0.0
    
    y0 = myFunction(a)
    yn = myFunction(b)
    
    for x in range(int(n/2) - 1):
        sumEven += myFunction(a + 2*h*(x+1))
        
    for x in range(int(n/2)):
        sumOdd += myFunction(a + h*(2*x + 1))
        
    total = (y0 + 4*sumOdd + 2*sumEven + yn)*(h/3)
    return total
 

# Used to determine the definite integral of myFunction between the limits a and b via the 
# composite Simpson's Rule (with n strips) rounded to the number of significant figures equal to
# a user input sigFig. It was determined graphically (using a relative error plot) that the 
# greatest achievable accuracy corresponds to n = 10000. This means the value of sigFig must not 
# exceded 14 or an incorrect value will be outputted.
def SimpsonsRuleSigFig(a, b, sigFig):
    if sigFig > 14 or sigFig < 1 or not isinstance(sigFig, int):
        raise ValueError('Please input an integer value of significant figures between 1 and 19 '
                          'in the form 1, 2, 3,... etc.')
        
    total = SimpsonsRule(a, b, 10000)
    return str(round(total, sigFig))

# Used to obtain the relative error from the Simpson's Rule against the analytical value between
# the limits a and b. 
# The number of data points, i, must be specified.
# Note: Values of i > 6 will require a substantial waiting time for the program to produce 
# an output. Additionally, values of i < 2 will fail to produce a line of best fit.
def SimpsonsErrorPlot(a, b, i):
    i+=1
    xValues = []
    yValues = []
    x = 1
    
    while x < i:
        yValues.append(np.log10(np.abs((SimpsonsRule(a, b, pow(10, x-1))/result) - 1)))
        xValues.append(x-1)
        x+=1
    
    
    fig = plt.figure()
    plt.scatter(xValues, yValues)
    
    fig.suptitle('Simpsons Rule: Relative Error', fontsize=14)
    plt.xlabel('log(n)', fontsize=12)
    plt.ylabel('log(Error)', fontsize=12)
    
    if i <= 6:
        a, b = best_fit(xValues, yValues)
        yfit = [a + b * xi for xi in xValues] 
        plt.plot(xValues, yfit)
        fig.suptitle('Simpsons Rule: Relative Error\ny = {:.2f} + {:.2f}x'.format(a, b), fontsize=10)

    
    plt.savefig('SimpsonsErrorPlot.jpg', dpi = 300)

    
    
# -------------------------------------------------------------------------------------------------
# Using the Scipy.integrate package
# -------------------------------------------------------------------------------------------------

# An additional available method from the Scipy.integrate package used in some
# calculations for the final report. 
def IntegralEvaluationVariable(a, b):
    result = quad(myFunction, a, b)
    return result


# -------------------------------------------------------------------------------------------------
# Line of Best Fit
# -------------------------------------------------------------------------------------------------

# A program to determine the line of best fit using the least-square method. 
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numerator = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denominator = sum([xi**2 for xi in X]) - n * xbar**2

    b = numerator / denominator
    a = ybar - b * xbar

    return a, b


# -------------------------------------------------------------------------------------------------
# Main Program
# -------------------------------------------------------------------------------------------------
# In this main program, the key graphs used in the report are obtained and saved locally. The 
# integrand can be changed by the user by replacing myFunction with a custom function. 

# First, the integrand itself is plotted and saved locally. To obtain a smooth visual curve
# n is set to 1000, while the limits are selected as 0 and pi respectively.
n = 100
xmin = 0
xmax = np.pi

plotFunction(myFunction, n, xmin, xmax)

# Next, the function is integrated by the trapezium rule. The relative error between the 
# analytical answer and numerical answer is calculated, as outlined in the description of the 
# method. Set the number of data-points to 6 for reasonable computational speed. 
x0 = 2

TrapeziumErrorPlot(xmin, x0, 6)

# A table is created of numerical results from the trapezium rule and stored locally in a 
# text file.
TrapeziumRuleTable(xmin, x0)

# Finally, create a plot for the Simpsons rule error. 
SimpsonsErrorPlot(xmin, x0, 5)