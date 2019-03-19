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

# BMI EXAMPLE

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
#FABONACHI EXAMPLE

# def fab(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-2)+fab(n-1)
#
# for i in range(1,11):       10 times = 1,11 (1,10 would be 9 times)
#     print(fab(i))

# ITERATIONS

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

#LETTERS AND THEIR VALUES

# name = 'Anna'
# for letter in name:
#     print(ord(letter))     #Shows the values for each of the letters separatedly

#calculate the value of your name
# total_value = 0
# name= 'Anna'
# for letter in name:
#     total_value = total_value + (ord(letter)-96)
#
# print(total_value)

#COUNTDOWN

# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')
# countdown(5)
#
#ORGANIZING LETTERS

# team = 'Celtics'
#
# print(len(team))
#
# letter=team[0]
# print(letter)
# letter=team[1]
# print(letter)
#
#
# letter=team[6]
# print(letter)
#
# print(team[len(team)-1])
#
# print(team[-7])
# print(team[-6])
# print(team[-5])
#
# for letter in team:
#     print(letter)

# prefixes = "JKLMNOPQ"
# # suffix = 'ack'
# # for letter in prefixes:
# #     if letter == 'O' or letter == 'Q':
# #         print(letter+'u'+suffix)
# #     else:
# #         print(letter+suffix)
#
# result = 0
# for number in range(1,1001):
#     if number % 2 == 1:   #% means the remainder of number/2
#         result = result + number
#
# print(result)            #it will give the sum of all the even numbers until 1000

#BACK AT PLAYING WITH LETTERS

# team="Celtics"
# print(team[0:5])
# print(team[:5])
# print(team[1:7])
# print(team[1:])
#
# print(team[::2])    #every other letter
# print(team[::-1])


# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
#
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter in 'Ee':
#         count = count + 1
# print(count)
#
# new_team = ""
# for letter in word:
#     if letter != 'a':
#         new_team = new_team+letter
# print(new_team)
#
# FINDS THE POSITION OF THE LETTER
# print(word.upper())   # capitalizes
#
# print(word.find('a'))    #finds the position

# a='anna'
# print(a==a[::-1])  #is it a palindrome?
# new_name = a[:2]+a[-1]
# print(new_name)

#REPLACE
# name= 'Anna'
# print(name.replace('n','m'))

#SPLI (removes the symbol)
# name='anna'
# print(name.split('n'))
#                            #result = ['a', '', 'a']

#STRIP (removes symbol - needs to remove leading character)
#print('www.example.com'.strip('cmowz.'))    #result = example
# print('anna'.strip('a'))     results in nn
# however print('anna'.strip('n')) does not work
# print('   spacious   '.strip())        #removes the space