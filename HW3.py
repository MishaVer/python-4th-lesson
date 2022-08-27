a_list = [1, 2, 2, 3, 3, 4]
b_list = []
for i in a_list:
    if i not in b_list:
        b_list.append(i)
print(b_list)