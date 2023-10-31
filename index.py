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

print(f"soma finalizada. resultado final = {resultado} ")

# Funções - Criando uma função:

print("Digite seu nome: ")
nome = (input())

def saudacao(nome):
    print("Oi " + nome +"! tudo bem? Seja bem vindo!")


# Função de soma:
def soma(nmr1,nmr2):
    print("digite dois números para obter a sua soma: ")
    nmr1 = int(input())
    nmr2 = int(input())
    op = nmr1 + nmr2
    print(op)

#loop de contagem regressiva:
def contagem_regressiva():
    meunumero = 11
    while meunumero > 1:
        meunumero = meunumero - 1
    print(meunumero)

# Soma de números pares:
def soma_dos_pares():
    soma = 0
    print("Digite um número para somarmos os algarismos pares até chegar no valor informado:")
    numero = int(input())
    
    while numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        for i in range(1, numero + 1):
            if i % 2 == 0:
                soma = soma + i

    print(" A soma dos números pares de 1 até ", numero, "é = ", soma)

def tabuada():

    print("insira um numero inteiro e positivo para calcularmos a sua tabuada: ")
    numero = int(input())

    while numero <= 0 :
        print("Número incorreto, informe um válido por favor.")
        numero = int(input())
    for i in range(1,11):
        res = numero * i
    print(f"{numero} x {i} = {res}")

def fatorial():

    print("Digite um número inteiro positivo para saber o seu fatorial:")
    numero = int(input())

    if numero < 0:
        print("Não existe fatorial para números negativos")
    elif numero == 0 :
        print("O fatorial de 0 é 1")
    else:
        for i in range(1, numero + 1):
            fatorial = fatorial * 1 
            print(fatorial)    
    
# Chamando uma função filha dentro de uma função pai:

def Main():
    print("eu sou a função pai.")

    def filho():
        print("Eu sou a função filho.")
    
    filho()

if __name__  == "__main__":   # conversão para exibir as duas funções.
    Main()


# Escreva um programa que calcule o numero de vogais em uma palavra.
print("Escreva uma vogal e veja quantas vogais ela possui")
palavra = (input())

vogais = ["a","e","i","o","u"]
contagem = 0

for letra in palavra:
    if letra in vogais:
        contagem = contagem + 1
print("O número de vogais na palavra ",palavra, "é igula a ", contagem)

# Invertendo Uma frase passo a passo:

# Tranformando uma frase em uma lista de palavras:
frase = "E - businnes é uma maneira de negócios relacionada com a tcnologia."
lista_de_palavras = frase.split()
#  invertendo a ordem das palavras:
frase = "I am luis"
palavras_listas = frase.split()
palavras_invertidas = frase[::-1]
#Juntando as palvras em uma frase invertida:
frases_invertidas = " ".join(palavras_invertidas)
#Função de inverter frase:
def inverter_frase(frase): 
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = " ".join(palavras_invertidas)
    print(frase_invertida)

frase_normal = (input())
frase_invertida = inverter_frase(frase_normal)
print(frase_invertida)

# Verficando se a palavra é um palíndromo
def palindromo():
    print("Digite uma palavra:")
    palavra = (input())
    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        print(palavra + " é um palíndromo!")
    else:
        print(palavra + " não é um palíndromo. resultado = " + palavra_invertida)

# removendo um carctere de uma frase usando o método replace():

def caractere():
    print("insira uma frase:")
    frase = (input())

    print("digite o caractere a ser removido:")
    caractere = (input())

    #usando método replace para substituir "caractere" por um esaço vazio em uma string
    Frase_sem_caractere = frase.replace(caractere, "")
    print(Frase_sem_caractere)

# Deslocando caracteres em uma frase usando a cifra de cesar:

def cifra_de_cesar():
    frase = (input("Escreva a frase:  "))
    deslocamento = int(input("Qual o deslocamento desejado?  "))
    frase_cifrada = "" #iniciando frase_cifrada sem valor para construir a frase letra por letra

    for caractere in frase:
        if caractere.isalpha():
            codigo = (ord(caractere) - ord("a"))
            novo_codigo = ( codigo + deslocamento) % 26 # uso "% 26" para que o codigo fique entre 0 e 25.
            novo_caractere = chr(novo_codigo + ord("a"))
            para_maiusculo = caractere.isupper()  # criando uma variável para verificar se a frase inserida esta toda em caracteres maiúsculos. 
            if para_maiusculo:
                caractere_maiusculo = caractere.upper()
                frase_cifrada = frase_cifrada + caractere_maiusculo
            else:
                frase_cifrada = frase_cifrada + novo_caractere
    print("a frase " + frase + " com o deslocamento usado fica = " + frase_cifrada)


    














































    



























































































