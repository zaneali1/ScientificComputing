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

The function chosen

## References
[1] Hoover, Dorothy M. (1955) "Estimates of Error in Numerical Integration," Journal of the Arkansas Academy of Science: Vol. 8 , Article
23.
