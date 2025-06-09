#1
def boas_vindas():
    print("Bem-vindo(a) à Disciplina ALLP")

boas_vindas()

#2
def quadrado(numero = 5):
    resultado = numero ** 2
    print(f"O quadrado de {numero} é: {resultado}")
    return resultado 
print(quadrado())

#3
def somar(a,b):
    return a + b

c = somar (1,6)
print(c)

#4
def contagem (início=1, fim=5):
    for numero in range (início, fim + 1):
        print (numero)
contagem(3,8)
#contagem()

#5
def calcula_imc(peso=70,altura=1.75):
    imc = peso/altura**2
    return imc

imc = calcula_imc()
print(f"O seu IMC é: {imc:.2f}")

#6
def par_ou_impar(numero):
    if numero % 2 == 0:
        print ("o número" , numero, "é par")
    else:
        print("O número" , numero, "é ímpar")

par_ou_impar(7)

#7
def saudacao(nome="Visitante"):
    print("Olá,", nome)

saudacao("Maria")
saudacao("João")

