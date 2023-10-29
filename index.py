# Verificando se um número é par ou impar:
print("Esse é um programa que verifica pra você se o número digitado é par ou impar.")

numero = int(input("digite o número:"))

if numero % 2 == 0:
    print("o número digitado é par.")
else:
    print("O número digitado é ímpar.")


# calculando a média de 3 notas e dependendo do valor mostrar um mensagem.
print("informe três notas para calcularmos a média e informar seu resultado.\n")

print("digite a primeira nota:")
nota1 = float(input())

print("digite a segunda nota:")
nota2 = float(input())

print("digite a terceira nota:")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

# usando if para comparar a média e informar a mensagem de acordo com o resultado:
if media >= 7:
    print(f"sua média é {media}, você está aprovado, parabéns!")
elif media < 7 and media >=5:
    print(f"sua média é {media}, você está de recuperação!")
elif media <5 :
    print(f"sua média é {media}, você está reprovado! estude mais na proxima.")
else:
    print("As notas que você informou são inválidas!")
# Para concatenar a variável float "media" que foi usada, usa-se "f" antes da mensagem em print e dentro de print passa a variável dentro
# de chaves.


# criando programa que informa ao usuário se o número que ele digitou é positivo, negativo, ou nulo.

print("Olá! digite um número e informaremos se ele é positivo, negativo ou nulo:")
numero = int(input("digite o número:"))
# usando if para comparar número digitado:
if numero > 0:
    print("O número digitado é positivo")
elif numero < 0:
    print("o numero digitado é negativo.")
else:
    print("O número que você digitou é nulo.")

# Dando valor a 4 variáveis e calculando a diferença entre as duas primeiras multiplicadas entre si, com as duas últimas também multiplicadas entre si.

a = int(input("dê um valor a primeira variável: "))
b = int(input("dê um valor a segunda variável: "))
c = int(input("dê um valor a terceira variável: "))
d = int(input("dê um valor a quarta variável: "))

diferenca = (a * b) - (c * d)

print(f" A diferença é = {diferenca}")


# programa que calcula o salário de um funcionário no dia, por horas trabalhadas:

print("Olá, me diga seu nome:")
nome_func = (input())

print("Oi " + nome_func + ", me diga seu número de funcionário na empresa:")
nmr_func = int(input())

print(nome_func +", quantas horas você trabalhou hoje? ")
hrs_trabalhadas = int(input())

print("Me informe quanto você ganha por hora, " + nome_func + ".")
salario_hrs = float(input())

# calculando salário final:
salario_final = hrs_trabalhadas * salario_hrs

print(f"numero de funcionário : {nmr_func}")
print("nome: " + nome_func)
print(f"Seu salário hoje é R$ {salario_final}")

# Programa que calcula o salário de um vendedor com um bonûs de comissão adicional:

print("Olá vendedor, qual o seu nome?")
nome = (input())

print("Me informe o seu salário fixo " + nome)
salario_fixo = float(input())

print("Certo " + nome +". Agora, me informe qual foi o seu valor total de vendas esse mês")
vendas = float(input())

# calculando salário final:
salario_final = salario_fixo + vendas * 0.15

print("Nome do vendedor: " + nome)
print(f"Vendas mensais: R$ {vendas}")
print(f"Salário = R$ {salario_final}")

# Programa que pede o código, o número e o valor de duas peças, para calcular o valor total depois:
 
print("Digite o código da peça escolida:")
codigo = int(input())
print("Quantidade de peças:")
qntd_pecas = int(input())
print("Valor da peça escolhida:")
valor_peca1 = float(input())

print("digite o código a segunda peça escolhida:")
codigo2 = int(input())
print("Quantidade de peças:")
qntd_pecas2 = int(input())
print("Valor da peça escolhida:")
valor_peca2 = float(input())

print("CONFIRMAÇÂO:")
print(f"Peça 1 = código: {codigo} --- quantidade de peças: {qntd_pecas} --- valor da peça: {valor_peca1}")
print(f"Peça 2 = código da peça: {codigo2} --- quantidade de peças: {qntd_pecas2} --- valor da peça: {valor_peca2}")

# calculando valor total:
valortotal = (qntd_pecas * valor_peca1) + (qntd_pecas2 * valor_peca2)

print(f"VALOR A PAGAR = R$ {valortotal}")


# Criando tipos de variáveis:

# Listas:
nomes = ["luis" , "felipe", "oliveira" , "silva", 19, 45, 34] #estilo de array.
#  Tuplas:
nomes = ("luis", "felipe", "oliveira" , "silva")
# dicionario:
nomes_e_idades = {"luis": 19, "oliveira" : 10, "silva": 13}

# Mudando tipo de variáveis:

# inteiro para float e vice e versa:
n1 = 10
print(float(n1))
l = 3.14
print(int(l))
# Números em strings:
numero = 15
print(type(str(numero)))


# Programa que imprime uma msg através da idade inserida:
 
print("Digite sua idade: ")
idade = int(input())

if idade >= 0 and idade <= 12:
    print("Idade de uma criança!")
elif idade >= 13 and idade <= 18:
    print("Idade de um adolecente!")
elif idade > 18 and idade <= 65:
    print("Idade de um adulto!")
else:
    print("Está na melhor idade.")


# loop for:

sabores_sorvetes = ["Maracujá" , "Morango" , "Ameixa", "Chocolate" , "Graviola"]
# Imprimindo lista de sabores:
for itens in sabores_sorvetes:
    print(itens)

# Loop while:

Idade_instrutor = 27
Minha_Idade = 0

while Minha_Idade < Idade_instrutor:
    Minha_Idade = Minha_Idade + 1
    print(Minha_Idade)
# programa que soma os números que estão sendo inseridos. Para parar a soma o usuário deve digitar 0

resultado = 0
print("Esse é um programa que soma os números que você esta inserindo.")
print("Para finalizar a soma e obter o resultado final, basta digitar 0.")

print("Digite o número:")
numero_soma = float(input())

while numero_soma != 0:
    resultado = resultado + numero_soma
    print(f"resultado da soma: {resultado}")
    
    print("Digite outro número para soma:")
    numero_soma = float(input())

# Funções - Criando uma função:

print("Digite seu nome: ")
nome = (input())

def saudacao(nome):
    print("Oi " + nome +"! tudo bem? Seja bem vindo!")

saudacao(nome)
# Função de soma:
def somar(a,b):
    return a + b
print(somar(10,40))



    
    



























































































