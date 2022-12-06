#Задайте список из нескольких чисел. Напишите
#  программу,
#  которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

#Пример:

#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

array = [2, 5, 5, 11, 3,5]

def find_posision_odd(array):
    '''функция принимает список и находит сумму эелементов стоящих на нечетных позициях'''
    sum = 0
    for i in range(len(array)):
        
        if i%2 !=0:
         
            sum+=array[i]
   
    return sum

print(find_posision_odd(array))

#Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний
#  элемент, второй и предпоследний и т.д.

#Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math

list1 = [2, 3, 4, 5, 6]

def find_product_pair(list1):
    '''функция принимает список и находит произведения пар чисел из
    списка, перемножая 1 число с последним, 2 с предпоследним и так до середины
    списка. Если в списке нечетное количество элементов, то центральное число 
    умножается само на себя'''
    new_list = list1[::-1]
    print(list1)
    print(new_list)
    product = [list1[i]*new_list[i] for i in range (len(list1))]
    if len(product)%2 == 0:
        stop = (len(product)/2)
        slice_object = slice(stop)
        product = product[slice_object]
    elif len(product)%2 != 0:
        stop = (math.floor(len(product)/2))+1
        slice_object2 = slice(stop)
        product = product[slice_object2]
    return product
    
print(find_product_pair(list1))

#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

import math

list_float = [4.07, 5.1, 8.2444, 6.9814]

def max_min(list_float):
    '''функция берет дробную часть числа, находит максимальное и минимальное, и 
    считает разницу между ними'''
    new_array = [((i%1)*100) for i in list_float]
    print(new_array)
    minimal = new_array[0]
    maximal = new_array[0]
    for i in new_array:
         if i <= minimal:
            minimal = i
    for i in new_array:
        if i >= maximal:
            maximal = i
    
    dif = (maximal - minimal)/100
    return dif
    
print(max_min(list_float))

# 4- Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10 

# print(int(input("Введите десятичное число  "))) 

def decimal_in_binary(dec_number):
    '''функция принимает на вход десятичное число и 
    преобразует его в бинарное'''
    dec_number = int(dec_number)
    num = ''
    while dec_number>0:
        num = str(dec_number%2) + num
        dec_number = dec_number//2
    return num
print(decimal_in_binary(int(input("Введите десятичное число  "))))  





#  5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,-13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

k = int(input('введите число:  '))
def febbon(k):
    fibo = []
    first,sec = 1,1
    for i in range(k-1):
        fibo.append(first)
        first,sec = sec,first+sec
    first,sec = 0,1
    for i in range(k):
        fibo.insert(0, first)
        first,sec = sec,first-sec
    return fibo

fibo = febbon(k)
print(febbon(k))
print(fibo.index(0))

#Задачу с фибоначчи посмотрела на семинаре, 
# сама запуталась и не решила. 
