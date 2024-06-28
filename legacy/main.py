from calculator import sum

# print(sum(10, 20))
# print(sum(-10, 20))
# print(sum(1.5, 2.5))

try:
    print(sum('1', 1))
except AssertionError as e:
    print(f'Conta inválida: {e}')
