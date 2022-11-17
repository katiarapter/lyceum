a = [1, 2, 3, 4, 5, 6]
for i in range(len(a) - 1, -1, -1):
    if a[i] % 2:
        a.pop(i)
    else:
        a[i] = a[i] // 2
print(a)
