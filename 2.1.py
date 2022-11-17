a = input()
# надо вввести строку, где числа надо вводить через пробел
spisok = a.split()
for elem in spisok:
    if elem == '237':
        break
    if int(elem) % 2 == 0:
        print(elem)
