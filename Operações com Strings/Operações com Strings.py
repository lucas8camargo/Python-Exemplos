nome='Lucas' 
print(f'Ola,{nome}!') 
 
 
x.upper() # Mostra a string toda em maiusculo 
x = x.upper() # Torna a string toda em maiusculo 
x.lower() # Mostra a string toda em minuscula 
x = x.lower() # Torna a string toda em minuscula 
x.tittle() # Torna primeira letra de cada palavra da string em maiuscula 
x = x.tittle() # Torna a string em formato tittle 
a.replace("H","J") # Substitui os caracteres 
a.split(",") # Separa as palavras em uma especie de lista o parametro define o que tem entre as palavras 
x.strip() # Remove os espaços (não entreaspalavras) 
x.lstrip() # Remove os espaços da esquerda 
x.rstrip() # Remove os espaços da direita 
x.find('y') # Mostra o espaço do primeiro caracter da palavra'y' 
x.count('y') # Mostra quantos caracteres ou palavras'y'estão na string 
x.swapcase() # Minusculas se tornam maiusculas e vice-versa 
print(x[y]) # Mostra o caracter na posição'y' 
len(x) # Mostra a quantidade total de caracter usado (espaços contam) 
 
# Acessando as index da string 
 
print(a[0]) 
print(a[0:10]) 
print(a[0:10:2]) 
print(a[-1]) 
print(a[-10:-1]) 

a[:] # Retorna toda a string
 
# A string segue a formatação da variavel 
 
a="""Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""
 
print(a) 
 
# Retornando True ou False 
 
x = "ain" in txt 
x = "ain" not in txt 
 
# Concatenação 
 
c = a + b 
 
# Concatenação adicionando uma string 
 
c = a +" "+ b 

\'  Single Quote 
\\  Backslash 
\n  New Line 
\r  Carriage Return 
\t  Tab 
\b  Backspace