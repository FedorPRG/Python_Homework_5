# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 10) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Учтено, что если коэффициент =0, то 0*х=0
import random
k=int(input('Введите натуральную степень k='))
spKoff=[]
for i in range(0,k+1):
    spKoff.append(random.randint(0,10))

line=''
for i in range(0,k+1):
    if i==0:
        if spKoff[i]>0:
            line=line+'+'+str(spKoff[i])+'=0'
        else:
            line=line+'=0'
    elif i==1:
        if spKoff[i]>1:
            line=str(spKoff[i])+'*x'+line
        elif spKoff[i]==1:
            line='x'+line
    else:
        if spKoff[i]>1:
            line=str(spKoff[i])+'*x^'+str(i)+'+'+line
        if spKoff[i]==1:
            line='x^'+str(i)+'+'+line
spKoff.reverse()            
print(spKoff)
print(f'{k=}->',line)