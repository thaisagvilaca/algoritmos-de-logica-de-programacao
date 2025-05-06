#código que verifica números pares, excluindo os números: 10, 20 e 30.

for n in range (0,31,2):
    if n == 10 or n == 20 or n == 30:
        continue
    print(n)
