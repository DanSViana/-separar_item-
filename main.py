# lista de frutas
frutas = ['Macujá', 'Maçã', 'Laranja', 'Banana', 'Uva', 'Abacaxi']

# exibe a lista e os índice
for i in range(len(frutas)):
    print(f'Fruta de índice {i}: {frutas[i]}.')

# usuário informa o índice do item a ser separado
indice = int(input('\nInfome o indice do item que deseja separar:'))

# separa o item 
fruta = frutas.pop(indice)

# exibe o item separado
print(fruta)

for i in range(len(frutas)):
    print(f'Fruta de índice {i}: {frutas[i]}.')