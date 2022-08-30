# Criação de arrays para uso no estudo
linguagens = ["python", "java", "c#", "php"]
adjetivos = ["fácil", "eficiente", "legal", "difícil"]

# 'For' apresentando as letras de uma string
for x in "python":
    print(x)

# 'For' apresentando os elementos de uma array
for x in linguagens:
    print(x)

# 'Break' parando o comando 'for'
for x in linguagens:
    print(x)
    if x == "c#":
        break

# Cancela o loop e continua com o próximo elemento
for x in linguagens:
    if x == "java":
        continue
    print(x)

# Sequência de números que começa em 0 e aumenta de 1 em 1 por padrão até o número anterior ao específicado
for x in range(10):
    print(x)

# Sequência de números definindo o número inicial
for x in range(5, 10):
    print(x)

# Sequência de números definindo o número inicial e o intervalo entre números
for x in range(5, 50, 10):
    print(x)

# Uso do 'else' no 'for'
for x in range(5):
    print(x)
else:
    print("Acabou!")

# O 'else' é cancelado se usarmos o 'break' antes do loop acabar
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("Acabou!")

# É possível rodar um loop dentro de outro
for x in adjetivos:
    for y in linguagens:
        print(x, y)

# É possível usar 'pass' para evitar um erro com um 'for' vazio
for x in [0, 1, 2]:
    pass