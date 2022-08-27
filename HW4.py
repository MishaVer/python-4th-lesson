import random

k = int(input())
stroka = ''

for i in range(k+1):
    if i == 0:
        stroka = stroka + str(random.randint(0, 100)) + '*x' + str(k-i)
    else:
        stroka = stroka + '+' + str(random.randint(0,100)) + '*x' + str(k-i)
print(stroka)