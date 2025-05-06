notas = 0
contador = 0

while contador < 2:
    entrada = (float(input('Digite a nota: ')))

    if entrada < 0 or entrada > 10:
        print('Nota inválida!')
        
    else:
        notas += entrada 
        contador += 1

media = notas/contador 

print(f"A sua média foi: {media} ")