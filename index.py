# Verificando se um número é par ou impar:
# print("Esse é um programa que verifica pra você se o número digitado é par ou impar.")

# numero = int(input("digite o número:"))

# if numero % 2 == 0:
#     print("o número digitado é par.")
# else:
#     print("O número digitado é ímpar.")


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




