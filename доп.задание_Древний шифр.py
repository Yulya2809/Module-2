res = ""

print("Введите любое положительное число от 3 до 20 включительно")
numEnter = int(input())

if 1 <= numEnter <= 2 or numEnter > 20:
    print("Введите числа согласно условию")
for i in range(1, numEnter + 1):
    for j in range(i + 1, numEnter + 1):
        pair_sum = i + j
        if numEnter % pair_sum == 0:
            res += str(i) + str(j)

print(res)

