import copy
from collections import deque
import numpy as np

#Creates a polynomial object by taking in a list of the coefficients a0,a1,...,an
class Polynomial:
    def __init__(self,coefficients_list):
        self.coefficients_list = coefficients_list
        self.order             = len(coefficients_list) - 1
    
    # Method evaluates at x
    def evaluate(self,x):
        p = 0
        for i in range(self.order+1):
            p += self.coefficients_list[i]*x**i
        return p

    def get_coeffs(self):
        return(self.coefficients_list)

    def get_order(self):
        return(self.order)
    
    def set_coeffs(self, coefficients_list):
        self.coefficients_list = coefficients_list
        self.order             = len(coefficients_list) -  1

    #Gets the polynomial object that is the derivative of the initial polynomial object
    def get_derivative(self):
        coeff_list = copy.copy(self.coefficients_list)
        for i in range(self.order+1):
            print(i)
            coeff_list[i] = self.coefficients_list[i]*i
        coeff_list.pop(0)
        if coeff_list == []:
            coeff_list = [0]
        return Polynomial(coeff_list)

    #Gets the polynomial object that is the antiderivative derivative of the initial polynomial object through (x,y)
    def get_antiderivative(self,x,y):
        coeff_list = copy.copy(self.coefficients_list)
        for i in range(self.order+1):
            print(i)
            coeff_list[i] = self.coefficients_list[i]/(i+1)
        coeff_deque = deque(coeff_list)
        coeff_deque.appendleft(0.0)
        coeff_list = list(coeff_deque)
        c = y - Polynomial(coeff_list).evaluate(x)
        coeff_list[0] = c
        return Polynomial(coeff_list)

#Gets point-value representation:
def point_values(poly,order):
    point_vals = []
    for i in range(order+1):
        point_vals.append((i, poly.evaluate(i)))
    return point_vals

#Interpolates
def interpolate(pvls):
    b = []
    xs = []
    n = len(pvls)
    for i in range(n):
        b.append(pvls[i][1])
        xs.append(pvls[i][0])
    b = np.transpose(np.array([b]))
    xs = np.array(xs)
    A = np.zeros((n,n))
    for i in range(n):
        A[:,i] = xs**i
    x = np.linalg.inv(A)@b
    coeffs = []
    for i in range(n):
        coeffs.append(x[i][0])
    return coeffs

#Multiplies two polynomial objects
def multiply_polys(poly1,poly2):
    new_order = poly1.get_order()+poly2.get_order()
    pvls1 = point_values(poly1,new_order)
    pvls2 = point_values(poly2,new_order)
    new_pvls = []
    for i in range(new_order+1):
        new_pvls.append((pvls1[i][0], pvls1[i][1]*pvls2[i][1]))
    new_coeffs = interpolate(new_pvls)
    return Polynomial(new_coeffs)


#Example:
my_poly = Polynomial([1,1,3])
#print(my_poly.evaluate(3))

deriv = my_poly.get_derivative()
#print(deriv.evaluate(6))

#print(my_poly.get_antiderivative(1,2).get_coeffs())

#print(point_values(my_poly,5))
poly1 = Polynomial([-1,1])
poly2 = Polynomial([1,1])

print(multiply_polys(poly1,poly2).get_coeffs())