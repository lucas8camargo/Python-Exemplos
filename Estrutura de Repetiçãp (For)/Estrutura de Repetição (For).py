fruits=["apple","banana","cherry"] 

for x in fruits: 
    print(x)
 
# For em uma string 
 
for x in"banana": 
    print(x)  
 
# O Continue é igual aocontinuedo C# 
 
fruits=["apple","banana","cherry"] 

for x in fruits: 
    if x == "banana": 
        continue 
print(x)
 
# O range define a quntidade de loops 
 
for x in range(6): 
    print(x) 
 
# A quantidade de loops pode ser um parametro "len()" 
 
a=[2,3,4,2,4,6]

for x in range(len(a)): 
        print(x) 
 
# Range com parametros de inicio (o ultimo é excluido) 
 
for x in range(2,6): 
    print(x) 
 
# Range com o ultimo parametro que define o salto 
 
for x in range(2,30,3): 
    print(x) 
 
#O else torna o for in range em uma especie de if 
 
for x in range(6): 
    print(x) 
else: 
    print("Finally finished!") 
 
# Fors aninhados 
 
adj=["red","big","tasty"] 
fruits=["apple","banana","cherry"] 

for x in adj: 
    for y in fruits: 
        print(x,y) 
 
# Um for não pode ser vazio mas é possivel criar um se o"Pass"for usado 
 
for x in[0,1,2]: 
    pass