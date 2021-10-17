number = int(input('Введите число: ')) #27644437 простое число
isPrime = True
for divider in range(2, number):
    if number % divider == 0:
        print('Делится на', divider)
        isPrime = False
        break
if isPrime:
    print(number, '- простое число')
else:
    print(number, '- составное число')