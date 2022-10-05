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

# print('Введите точку координат А:')
# x_A = float(input('X: '))
# y_A = float(input('Y: '))
# print("Введите точку координат B:")
# x_B = float(input('X: '))
# y_B = float(input('Y: '))

# from math import sqrt
# print('Расстояние между точками: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))

            # Посчитать сколько раз символ встречается в строке.

# string = "Посчитать сколько раз символ встречается в строке."
# res = 0
# simb = input("Ведите символ: ")
# for i in string:
#     if i == simb:
#         res += 1
# print(res)        

             #   Вывести из секунд колличество минут, чаcов, дней

# a = 100
# sec=a - (a//60)*60
# min=a//60-((a//60//60)*60)
# hh=a//60//60-((a//60//60//24)*24)
# day=a//60//60//24-((a//60//60//24//365)*365)
# print(f"{day} дней, {hh}:{min}:{sec}:")
  
            # ДРУГОЕ РЕШЕНИЕ
# sec = int(input(""))
# min, sec = sec // 60, sec % 60 
# hour, min = min // 60, min % 60
# day, hour = hour //24, hour % 24
# print(f"{day}:{hour}:{min}:{sec}")          

     # НАПИСАТЬ ПРОГРАММУ КОТОРАЯ ПРИНИМАЕ НА ВХОД ЧИСЛО N И ВЫДАЕТ ПОСЛЕДОВАТЕЛЬНОСТЬ ИЗ N ЧЛЕНОВ

# n = int(input())
# for i in range(n):
#     print((-3) ** i, end=" ")
 
    #  Для натурального n создать словарь индекс-значение, 
    #  состоящий из элементов последовательности 3n + 1.

# n = int(input("Введите натуральное число: "))
# dict = {}
# for i in range(1, n+1):
#     dict[i] = 3*i+1
#     print(dict)

    # Напишите программу, которая принимает на вход число N
    #  и выдает набор произведений чисел от 1 до N.

# n = int(input("Введите чило: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=" ")

    # Задайте список из n чисел последовательности (1+ (1/n))^n
    #  и выведите на экран их сумму.

# n = int(input("Введите число "))
# lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

# Найти позицию второго вхождения строки в списке или сообщить что её нет
# text_1 = ["qwe", "asd", "zxc", "ertqwe"]
# key_word = "qwe"
# def find_coincidence(new_text, key):
#     count = 0   
#     for i in range(len(new_text)):
#         if new_text[i] == key:
#             count += 1
#             if count ==2:
#                 print(i)
#                 break
            
#         if count < 2:
#             print("-1")
# find_coincidence(text_1, key_word)  



     



     #Задайте список из нескольких чисел. Напишите программу,
     # которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# a = [2, 3, 6, 10, 12, 16, 5]
# summ = 0
# for i in range(1, len(a), 2):
#     #if i % 2 == 1:
#         summ += a[i]
# print(f"{a} сумма элементов на нечётных позициях: {summ}")   

     # Напишите программу, которая найдёт произведение пар чисел списка. 
     # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)


    # Задайте список из вещественных чисел. Напишите программу,
    #  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)

    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -14
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2
# list = [0]
# userNumber = int(input('Enter any number: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)