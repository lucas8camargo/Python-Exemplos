# Um teste de True ou False pode ser feito em uma 
# lista de possíveis valores que a variável pode ter. 

op=input('Escolha uma opção')
 
if op not in['l','i','r','s']:
    print('Opção inválida')
else:
    print(f'Opção escolhida: {op}')