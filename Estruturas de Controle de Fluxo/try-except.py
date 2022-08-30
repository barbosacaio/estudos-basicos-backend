# Não executa porque o 'x' não foi definido e segue para o bloco de 'except'
try:
    print(x)
except:
    print("Houve uma exceção")

# Executa uma 'exception' dependendo do erro específico
try:
    print(x)
except nomeErro:
    print("Houve um erro específico")
except:
    print("Houve outro erro")

# O 'else' é executado se não houver nenhum erro
try:
    print("Olá, mundo!")
except:
    print("Houve um erro")
else:
    print("Não houve nenhum erro")

# O 'finally' é executado independente do que aconteceu no 'try except'
try:
    print(x)
except:
    print("Houve um erro")
finally:
    print("Acabou o 'try except'")

# Usar uma 'exception' se uma condição for verdadeira
x = 10
if x != 10:
    raise Exception("Desculpe, este número não é igual a 10")

# Usar uma 'exception' de acordo com o tipo da variável
y = "String"
if not type(y) is int:
    raise TypeError("Somente números inteiros são permitidos")