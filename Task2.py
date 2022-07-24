# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def func(x):
    spRezult=[]
    n=2
    while x>1:
        if x%n==0:
            spRezult.append(n)
            x/=n
        else:
            n+=1
    return spRezult

x=int(input('Введите натуральное число: '))
print(f'Список простых множителей числа {x} ->',func(x))