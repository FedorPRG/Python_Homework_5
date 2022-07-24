# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def funcwrite(text,spKoff): # записываем набор коэффициентов в файл
    with open(text,'w',encoding='utf-8') as file: 
        for i in spKoff:
            file.write(f'{i} ')    
    return

def funcread(text): # считываем набор коэффициентов из файла и преобразуем в список int
    spKoff=[]
    with open(text,'r',encoding='utf-8') as file: 
        a=file.readline().split(' ')
        for i in range(0,len(a)-1): 
            spKoff.append(int(a[i]))
    return spKoff

import random
k=int(input('Введите натуральную степень k=')) # размер многочлена
spKoff1=[]
spKoff2=[]
for i in range(0,k+1):
    spKoff1.append(random.randint(-10,10))# формируем набор коэффициентов
    spKoff2.append(random.randint(-10,10))# формируем набор коэффициентов
funcwrite('file1.txt',spKoff1)
funcwrite('file2.txt',spKoff2)
spKoff3=[]
spKoff3=funcread('file1.txt')
print(spKoff3,'- Первый список коэффициентов многочлена')
spKoff4=[]
spKoff4=funcread('file2.txt')
print(spKoff4,'- Второй список коэффициентов многочлена')
spKoff5=[]
for i in range(0,len(spKoff3)): # сумма многочленов - это сумма коэффициентов многочленов
    spKoff5.append(spKoff3[i]+spKoff4[i])
print(spKoff5,'- сумма коэффициентов многочленов')
spKoff5.reverse() 
line=''
for i in range(0,k+1):
    if i==0:
        if spKoff5[i]>0:
            line=line+'+'+str(spKoff5[i])+'=0'
        elif spKoff5[i]<0:
            line=line+str(spKoff5[i])+'=0'
        else:
            line=line+'=0'
    elif i==1:
        if spKoff5[i]>1:
            line=str(spKoff5[i])+'*x'+line
        if spKoff5[i]<1:
            line='('+str(spKoff5[i])+'*x)'+line            
        elif spKoff5[i]==1:
            line='x'+line
    else:
        if spKoff5[i]>1:
            line=str(spKoff5[i])+'*x^'+str(i)+'+'+line
        elif spKoff5[i]<1:
            line='('+str(spKoff5[i])+'*x^'+str(i)+')+'+line            
        elif spKoff5[i]==1:
            line='x^'+str(i)+'+'+line
print(line)
funcwrite('fileSumma.txt',line)
