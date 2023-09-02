# def divide(a, b): 
#     if b == 0:
#         return None
#     return a / b

# def divide(a, b): 
#     if b != 0: # ! (b ! = 0) сократили код не меняя логики
#         return a / b

# print(divide(10, 0))

from decimal import Decimal

def divide_n_times(value, divader, times):
    value = Decimal(value)
    for i in range(times):
        value /= divader
    # return value
    print(value)

divide_n_times(12345, 10, 5)