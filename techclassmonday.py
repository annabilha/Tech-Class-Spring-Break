# CREATE A FUNCTION

# def function_name(a):
#     result=function itself
#     return result
# or
# def function_name(a):
#    return=function itself
#
#
#  EXAMPLE
# def square_plus_one(a):
#     result=a**2+1
#     return result
# or
# def square_plus_one(a):
#     return a**2+1

# print(square_plus_one(3))  will give 10 as the result

# EXAMPLE 2
# def ahh(a,b):
#     return a+b
#
# print(ahh("pen", "notebook"))

#
# def quadratic(a, b, c):
#     return (-b+((b**2)-(4*a*c))**(1/2))/2*a, (-b-((b**2)-(4*a*c))**(1/2))/2*a
# or

# import math
# def quadratic(a, b, c):
#     x_1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
#     x_2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
#     return x_1, x_2
#
# print (quadratic(1,2,-3))      results are 1 and -3

#
# x=input("What is your weight?")
# x=float(x)
# y=input("What is your height?")
# y=float(y)
#
#
# def BMI(x,y):
#     return x/(y**2)
#
#
# if BMI(x,y) >= 30:
#     print("Obese")
# elif 29.9 >= BMI(x,y) >= 25:
#     print("Overweight")
# elif 24.0 >= BMI(x,y) >= 18.5:
#     print("Normal Weight")
# elif BMI(x,y) < 18.5:
#     print("Underweight")
#
# def fab(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-2)+fab(n-1)
#
# for i in range(1,11):       10 times = 1,11 (1,10 would be 9 times)
#     print(fab(i))

# sum=0
# for i in range(1,5):
#     print('in the {}th iteration, current i is {}, sum is {}'.format(i,i,sum))
#     sum=sum+i
#     print('\tafter adding i, the new sum is {}\n'.format(sum))
#
# sum=0
# for i in range(1,5):
#     print('in the {}th iteration, current i*i is {}, sum is {}'.format(i,i*i,sum))
#     sum=sum+i*i
#     print('\tafter adding i, the new sum is {}\n'.format(sum))
#

# name = 'Anna'
# for letter in name:
#     print(ord(letter))

#calculate the value of your name
# total_value = 0
# name= 'Anna'
# for letter in name:
#     total_value = total_value + (ord(letter)-96)
#
# print(total_value)
