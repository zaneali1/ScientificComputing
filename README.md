# Numerical Integration
*NB: A detailed write-up of this project can be found in this repository in the file NumericalIntegrationTechniques.pdf*.

## Overview
The definite integral of a function can be computed numerically using the Trapezium or Simpson's Rule. The Trapezium rule evaluates the area under a graph *f(x)* as a set of trapezia with straight line segments while the Simpson's Rule uses segments with parabolic curves. The techniques are approximations of the definite integral and have lower- and upper-bound error values which can be found analytically. For the Trapezium Rule, the error can be found as: [1]
<p align="center">
<img src="https://github.com/zaneali1/ScientificComputing/blob/main/READMEimages/ErrorT.PNG" width="160"/>
</p>

where *a* and *b* are the limits of the definite integral, *n* is the number of subintervals for the trapezia and ξ is an adjustable parameter which exists somewhere between *a* and *b*. For the Simpson's Rule, the error can be found as: [1]
<p align="center">
<img src="https://github.com/zaneali1/ScientificComputing/blob/main/READMEimages/ErrorS.PNG" width="160"/>
</p>

In this project, the Simpson's Rule, Trapezium Rule and a Python scipy.integrate package are used to evaluate a definite integral, and the error values are compared to the expected value in the first two instances. 

## Program
The program NumericalIntegration.py uses a function with limits, which can be user-defined, to produce a set of plots and data which are evaluated in the report NumericalIntegrationTechniques.pdf. An overview of the outputs of the program are as follows:
- **Function.jpg:** A plot of the function exp(-x)sin(x) between 0 and π, which is to be to be integrated using different numerical integration techniques 
between the limits 0 and 2. The range, function and limits can all be defined by the user. 

- **TrapeziumRuleTable:**: A table of approximations for the integral of the function provided to numericalintegration.py which have been calculated by the 
trapezium rule, where n is the number of trapezia. 

- **TrapeziumErrorPlot:** Plot of the relative error against the number of subintervals for the Trapezium Rule using a log10 - log10 scale.

- **SimpsonsErrorPlot:**  Plot of the relative error against the number of subintervals for the Simpsons Rule using a log10 - log10 scale.




## References
[1] Hoover, Dorothy M. (1955) "Estimates of Error in Numerical Integration," Journal of the Arkansas Academy of Science: Vol. 8 , Article
23.
