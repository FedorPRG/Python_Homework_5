# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

spisok=input('Задайте последовательность чисел через пробел: ').split(' ')
spisok = [int(x) for x in spisok]
spisok1=[1]
for i in range(1,len(spisok)):
    for j in range(0,i):
        cond=True
        if spisok[j]==spisok[i]:
            cond=False
            break
    if cond==True:
        spisok1.append(spisok[i])
print(spisok, '->', spisok1)