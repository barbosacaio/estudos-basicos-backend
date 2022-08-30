# Criação de variáveis para o estudo
a = 5
b = 10
c = 15

# Comparadores
if a == b:
    print("'a' é igual a 'b'")

if a != b:
    print("'a' é diferente de 'b'")

if a > b:
    print("'a' é maior que 'b'")

if a < b:
    print("'a' é menor que 'b'")

if a >= b:
    print("'a' é maior ou igual a 'b'")

if a <= b:
    print("'a' é menor ou igual a 'b'")

# 'if else'
if a == b:
    print("'a' é igual a 'b'")
else:
    print("'a' não é igual a 'b'")

# 'elif'
if a > b:
    print("'a' é maior que 'b'")
elif a < b:
    print("'a' é menor que 'b'")
else:
    print("'a' é igual a 'b'")

# Executando 'if' em uma linha
if a == b: print("'a' é igual a 'b'")

# Executando 'if else' em uma linha
print("'a' é maior que 'b'") if a > b else print("'a' é menor que 'b'")

# 'and'
if a < b and c > a:
    print("As duas condições são verdadeiras")

# 'or'
if a < b or c > a:
    print("Pelo menos uma das condições é verdadeira")

# Um 'if' dentro de outro 'if'
if a > 1:
    print("Maior que 1,")
    if a > 2:
        print("e maior que 2")
    else:
        print("mas não maior que 2")

# Use 'pass' para deixar um 'if' vazio sem ter erros
if a > b:
    pass