casa = {'quartos' : 3, 'banheiros' : 2, 'salas' : 2, 'cozinha' : 1, 'lavanderia' : 1, 'televisores' : 3, 'ventiladores': 3, 'mesas' : 2, 'computadores' : 2, 'microondas' : 1}
print(casa ['quartos'])
print(casa['banheiros'])
print(casa.keys())
print(casa.values())
print('cômodos' in casa)
del casa['lavanderia']
casa['escada'] = 1
casa['ventiladores'] = 4
print(casa.get('terraço', 'Não encontrado!'))
