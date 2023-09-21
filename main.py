# Задача 22
import numpy as np #
n=int(input("введите количество элементов 1 множества "))
m=int(input("введите количество элементов 2 множества "))

array_1=[]*n
for i in range(n):
    array_1.append(int(input(f'Введите значение элемента {i+1} множества 1 ')))

array_2=[]*m
for i in range(m):
    array_2.append(int(input(f'Введите значение элемента {i+1} множества 2 ')))

array_1=np.union1d(array_1,array_2)
print(array_1)


# Задача 24
# from random import randint

# n=int(input("введите количество кустов на грядке: "))
# list_1=list()

# for i in range(n):
#     list_1.append(randint(50,100))
#     print(f'{i}', end=" ")
# print( )

# max=0
# while n>0:
#     sum=list_1[-n]+list_1[-n+1]+list_1[-n+2]
#     print(f'{sum}', end=' ')
#     if sum>max:max=sum
#     n-=1
# print( )
# print(max)