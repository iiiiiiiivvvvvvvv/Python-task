#while original!=0:
#inverter=0
#while original!=0:
 #inverted=inverted*10+(original%10)
 #original//=10
#print(inverted) 

#for i in 2,3,4,5,6,7:
 #print(i**2)

#r = range(10)
#for i in range(0, 100,2):
 #print(i)

#text="Съешь еще этих мягких французских булок"

#print(text[0:])

#from tokenize import Number


#numbers=[1,2,3,4,5]
#print(numbers)

#ran=range(1, 6)
# #print(type(ran))
# #numbers=list(ran)
# #print(type(numbers))

# #a= int(input("Введите число A "))
# #print(a)
# #b= int(input("Введите число B "))
# #print(a**2==b)or(b**2==a)

# # Найти MAX из пяти чисел

# ЗАДАНИЕ СЕМИНАР 1

#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

# day = int(input("Введите номер дня недели "))
# if day > 7 or day < 1:
#      print("Повторите")
# elif day==6 or day==7:
#      print("Выходной день") 
# else:
#     print("Рабочий день")

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input("Введите координату X "))
# y = int(input("Введите координату Y "))
# if x > 0 and y > 0:
#     print("1 четверть")
# if x > 0 and y < 0:
#     print("2 четверть")
# if x < 0 and y < 0:
#     print("3 четверть")
# if x < 0 and y > 0:
#     print("4 четверть")        

#Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).

# n=int(input("Введите номер четверти "))
# if n < 1 or n > 4:
#     print("Повторите ввод ")
# elif n == 1:
#     print("x > 0 and y > 0")   
# elif n == 2:
#     print("x > 0 and y < 0")       
# elif n == 3:
#     print("x < 0 and y < 0")  
# elif n == 4:
#     print("x < 0 and y > 0")          

# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

print('Введите точку координат А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите точку координат B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Расстояние между точками: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))