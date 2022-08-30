# Criação de variáveis para o estudo
i = 1

# Printar 'i' enquanto ele for menor que 10
while i < 10:
    print(i)
    i += 1

# Sair do loop quando 'i' for igual a 5
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# Pular um elemento no loop
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

# Uso do 'else' no 'while'
while i < 10:
    print(i)
    i += 1
else:
    print("'i' não é mais menor que 10")