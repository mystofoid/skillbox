
# Число x является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x

n = int(input("n = "))
cycle = 0
lst = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0: # если делитель найден, число не простое.
          break
    else:
        lst.append(i)
        cycle += 1
print(cycle, lst)
