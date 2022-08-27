n=int(input())
for i in range(1, n+1):
    if(n%i==0):
        print(i)

b=int(input())
l_list = []
c = 2
while b != 1:
    if b % c == 0:
        l_list.append(c)
        b = b // c
    else:
        c = c + 1
print(l_list)
