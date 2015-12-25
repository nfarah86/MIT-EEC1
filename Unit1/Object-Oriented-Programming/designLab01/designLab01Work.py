# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

print("------------------------------ 1.3.1  --------------------------------")

def fib(n):
    # Delete the pass statement below and insert your own code
    if ((n == 1) | (n ==0)):
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(5))

#-----------------------------------------------------------------------------

print("------------------------------ 1.3.2  --------------------------------")
class CarNew:
    color = 'gray'

    def describeCar(self):
        return 'A cool ' + CarNew.color + ' car'


    def describeSelf(self):
        return 'A cool ' + self.color + ' car'

# nona = CarNew()
# print (nona.describeCar())
# print (nona.describeSelf())
# print (nona.color)

# print("\n")

# lola = CarNew()
# lola.color = 'plaid'
# print (lola.describeCar())
# print (lola.describeSelf())

# print("\n")

# print (nona.describeSelf())

# print("\n")

# nona.size = 'small' 
# # print (lola.size) # error

# print("\n")

# CarNew.size = 'big'
# print(lola.size )
# print(nona.size)


# print("\n")


print("------------------------------ 1.3.3  --------------------------------")


class Car:
    weight = 1000

    def __init__(self, weight, driver):
        self.weight = weight
        self.driver = driver

class Person:
    weight = 100

    def __init__(self, weight):
        self.weight = weight

# p = Person(150)
# print(Person) # class Personn back
# print(p) # instance of Person Object
# print("\n")
# print(Car.weight)
# c = Car(2000, p)
# print (c.weight)
# print("\n")

print("------------------------------ 1.3.4  --------------------------------")

class V2(object):
    def __init__(self, x, y):
        self.x_vector = x
        self.y_vector = y
        self.x_y_array = [x, y]


    def __str__(self):
        return str(self.x_y_array[0]) + " and " + str(self.x_y_array[1])
    
    def get_x(self):
        return self.x_y_array[0]

    def get_y(self):
        return self.x_y_array[1]

    def add(self, v):
        x_value = self.x_y_array[0] + v.x_y_array[0]
        y_value = self.x_y_array[1] + v.x_y_array[1]
        return (x_value, y_value)

    def mult(self, integer):
        x_value = self.x_y_array[0] * integer
        y_value = self.x_y_array[1] * integer
        return (x_value, y_value)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, integer):
        return self.mult(integer)

    def __repr__(self):
        return str(self)

# a = V2(1, 2)
# b = V2(3, 4)

# print (a.__add__(b))
# print (a.__repr__())
# print(a.get_y())
# print(a.__mul__(-1))
# new_v2 = a.__mul__(-1)
# print (new_v2)
# print (V2(1.1, 2.2) + V2(3.3, 4.4)) # uses __add__
# print("\n")

print("------------------------------ 1.3.5  --------------------------------")

import cmath
import math 


class Polynomial:


    def __init__(self, polynomial):

        self.polynomial = polynomial
        
        # initalize where self._polynomial[i][0] = coeff.
        # and self._polynomial[i][1] = the degree of power ie 2 = squared.
        # returns [(1,2),(2,1)(3,0)] for a 2 degree polynomial
        self._polynomial = [(polynomial[x], len(polynomial) - x - 1) for x in
                            range(len(polynomial))]

        self.degree = len(polynomial)


    def __len__(self):
        return len(self._polynomial)


    def __call__(self, integer):
        """
        Call the object and subsitutes the variable with integer.
        Returns a value
        """
        
        values = 0

        for i in self._polynomial:
            values += i[0] * (integer ** i[1])

        return values


    def __str__(self):
        
        string_representation = ""
        for i in self._polynomial:
            if i[1] == 1:
                string_representation += str(i[0]) + "z" + " + "
            elif i[1] == 0:
                string_representation += str(i[0]) + " "
            else:
                string_representation += str(i[0]) + "z**" + str(i[1]) + " + "
        return string_representation

    
    def add(self, other):
        """
        Adds two polynomial objects.  Returns a polynomial object
        """

        sum_dict = {}
        sum_values = 0
        sum_list = []

        for i in self._polynomial:
            if i[1] not in sum_dict:
                for j in other._polynomial:
                    print(i[1])
                    if i[1] == j[1]:
                        sum_values += j[0]
                sum_values += i[0]
                sum_dict[i[1]] = sum_values
                sum_values = 0

        for i in range(len(sum_dict)):
            sum_list.insert(i, sum_dict[len(sum_dict)-i-1])
        print(sum_list)
        return Polynomial(sum_list)


    def __add__(self, other):
        return self.add(other)


    def roots(self):
        """
        Find the roots of the polynomial. Number can be real
        or imaginary.  Returns a list.
        """

        if len(self) > 3:
            return "order is too high"
        
        elif self.degree == 3:
            # use quad. formula
            print (self._polynomial)
            b_square = self._polynomial[1][0] ** 2
            quad_term = 4*(self._polynomial[0][0])*(self._polynomial[2][0])
            dividend = 2 * (self._polynomial[0][0])
            first_root = (-1 * self._polynomial[1][0]) + cmath.sqrt(b_square - quad_term)
            second_root = (-1 * self._polynomial[1][0]) - cmath.sqrt(b_square - quad_term)
            return[first_root/dividend, second_root/dividend]

        elif self.degree == 2:
            #solve for x
            constant_value = -1.0 * (self._polynomial[1][0])
            root_value = constant_value / self._polynomial[0][0]
            return [root_value]
        
        elif self.degree == 1:
            return None
        
        else:
            return None


    def mult(self, other):
        """
        A polynomial object can be multiplied by itself or
        an integer.  Returns a polynomial object
        """

        if isinstance(other, int) or isinstance(other,float):
            value_mult = [x[0] * other for x in self._polynomial]
            return Polynomial(value_mult)
        
        elif isinstance(other, Polynomial):
            multiplied = []
            product = []
            sum_value = 0
            dict_degree = {}

            for x in self._polynomial:
                # mult = [(x[0] * y[0], x[1] + x[1]) for y in other._polynomial]
                for y in other._polynomial:
                    mult_value = [(x[0] * y[0], x[1] + y[1])]
                    multiplied.append(mult_value)

            # check to see if the degree values were the same as before
            for k in range(len(multiplied)):
                if multiplied[k][0][1] not in dict_degree:
                    for l in range(1+k, len(multiplied)):
                        if (multiplied[k][0][1] == multiplied[l][0][1]):
                            sum_value += multiplied[l][0][0]
                    sum_value += multiplied[k][0][0]
                    dict_degree[multiplied[k][0][1]] = sum_value
                    sum_value = 0

            # return a list
            dict_length = len(dict_degree)
            for i in range(len(dict_degree)):
                product.insert(i, (dict_degree[dict_length-i-1]))

            # print(str(product))
            return Polynomial(product)


    def __mul__(self, other):
        return self.mult(other)


# p1 = Polynomial([1, 2, 3])
# print(p1.__repr__())
# # print(p1.substitue_z(1))
# p2 = Polynomial([100, 200])
# print(p1 * p2 + p1)
# # print(p1(1))
#print((p1 + p2)(10))
# print(p1.coeff(-1))
# print("---- \n")
#print(p1.degree)

#product = (p1.mult(p1))
# product = (p2(2))
# print(product.__str__())
# print(p2.roots())
# product = p1 * p1
# print(product)
# print((p1*p1).roots())















