# Funções Python

def saudacao():
    print("Olá, Mundo!")

# Funções com Argumentos

def saudacao_personalizado(nome):
    print("Olá,", nome = "!")

saudacao_personalizado("Maria")

# Funções com Retorno

def soma(a, b):
    resultado = a + b 
    return resultado

total = soma(3, 5)
print(total)

# Exemplos Práticos

# Exemplo 01 

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicador(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    
    else:
        return x / y
    
# Exemplo 02

# Obtendo entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Menu de operações
print ("Escolha a operações:")
print ("1. Somar")
print ("2. Subtrair")
print ("3. Multiplicar")
print ("4. Dividir")

escolha = input("Digite sua escolha (1/2/3/4): ")

# Realizando a operação e exibindo o resultado
if escolha == '1':
    print(num1, "+", num2, "=", somar(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtrair(num1, num2))
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicador(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", dividir(num1, num2))

else: 
    print("Escolha inválido!")

