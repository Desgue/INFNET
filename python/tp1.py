import random

#Exercicio 1
def solicitar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def calcular_operacoes(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)"
    divisao_inteira = num1 // num2 if num2 != 0 else "Indefinido (divisão por zero)"
    
    return soma, subtracao, multiplicacao, divisao, divisao_inteira

""" num1, num2 = solicitar_numeros()
soma, subtracao, multiplicacao, divisao, divisao_inteira = calcular_operacoes(num1, num2)
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}") """


#Exercicio 2
#Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.
def min_to_hour(total_min ): 
    return (total_min // 60, total_min & 60)
def hour_to_min(hours, min):
    return hours * 60 + min

print("\\\\ EXERCICIO 2 //")
print("\r", min_to_hour(4505))
print("\r", hour_to_min(45, 47))

#Exercicio 3
def combinar_nomes(nome1, nome2):
    metade1 = nome1[:len(nome1) // 2]
    metade2 = nome2[len(nome2) // 2:]
    
    combinacoes = [
        metade1 + metade2,
        nome1[:2] + nome2,
        nome1 + nome2[-2:],
        nome1 + "_" + nome2,
        nome2 + "_" + nome1,
        nome1 + str(random.randint(0, 99)),
        nome2 + str(random.randint(0, 99)),
        f"{nome1}{random.choice(['X', 'Pro', 'Master', 'King'])}{nome2[-2:]}"
    ]
    
    return random.choice(combinacoes)

nome1 = input("Digite o primeiro nome de usuário: ")
nome2 = input("Digite o segundo nome de usuário: ")

nome_combinado = combinar_nomes(nome1, nome2)
print("Nome combinado:", nome_combinado)


# Exercicio 4
def calculadora():
    operacao = input("Escolha uma operação (adição, subtração, multiplicação, divisão): ").strip().lower()
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "adição":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "multiplicação":
        resultado = num1 * num2
    elif operacao == "divisão":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"
    
    return f"Resultado: {resultado}"

# Exemplo de uso:
print(calculadora())

# Exercicio 5
def saudacao_personalizada():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    return f"Olá, {nome} {sobrenome}! Bem-vindo!"

# Exemplo de uso:
print(saudacao_personalizada())

# Exercicio 6
def adivinhar_numero_secreto():
    numero_secreto = 42
    palpite = int(input("Adivinhe o número secreto: "))

    if palpite == numero_secreto:
        return "Parabéns! Você acertou!"
    elif palpite > numero_secreto:
        return "Muito alto!"
    else:
        return "Muito baixo!"

# Exemplo de uso:
print(adivinhar_numero_secreto())

# Exercicio 7
def calcular_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        status = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        status = "Peso normal"
    elif 25 <= imc < 29.9:
        status = "Sobrepeso"
    else:
        status = "Obesidade"
    
    return f"Seu IMC é {imc:.2f}. {status}"

# Exemplo de uso:
print(calcular_imc())

# Exercicio 8
def verificar_maioridade():
    idade = int(input("Digite sua idade: "))
    return "Você é maior de idade." if idade >= 18 else "Você é menor de idade."

# Exemplo de uso:
print(verificar_maioridade())

# Exercicio 9
def aplicar_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25
    elif valor_compra > 200:
        desconto = 0.15
    elif valor_compra > 100:
        desconto = 0.10
    else:
        desconto = 0.0

    valor_final = valor_compra * (1 - desconto)
    return f"Valor com desconto: R${valor_final:.2f}"

# Exemplo de uso:
valor = float(input("Digite o valor da compra: R$"))
print(aplicar_desconto(valor))

# Exercicio 10
import random

def criar_historia():
    personagens = ["um cavaleiro", "uma princesa", "um dragão", "um mago"]
    acoes = ["lutou bravamente", "fugiu apressadamente", "fez um feitiço", "encontrou um tesouro"]
    locais = ["na floresta", "em uma caverna", "no castelo", "no vilarejo"]

    historia = f"{random.choice(personagens)} {random.choice(acoes)} {random.choice(locais)}."
    return historia

# Exemplo de uso:
print(criar_historia())

# Exercicio 11
def simular_dados():
    num_dados = int(input("Quantos dados deseja lançar? "))
    resultados = [random.randint(1, 6) for _ in range(num_dados)]
    return f"Resultados: {resultados}"

# Exemplo de uso:
print(simular_dados())

# Exercicio 12
def classificar_palavras():
    palavras = input("Digite palavras separadas por espaço: ").split()
    classificadas = {"curtas": [], "longas": []}
    
    for palavra in palavras:
        if len(palavra) < 5:
            classificadas["curtas"].append(palavra)
        else:
            classificadas["longas"].append(palavra)

    return classificadas

# Exemplo de uso:
print(classificar_palavras())

# Exercicio 13
def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
    return "É um palíndromo!" if texto == texto[::-1] else "Não é um palíndromo."

# Exemplo de uso:
print(verificar_palindromo())

# Exercicio 14
def votacao():
    votos = {"Opção 1": 0, "Opção 2": 0, "Opção 3": 0}
    
    for _ in range(3):
        voto = input("Vote em Opção 1, Opção 2, ou Opção 3: ").strip()
        if voto in votos:
            votos[voto] += 1
        else:
            print("Voto inválido.")
    
    return votos

# Exemplo de uso:
print(votacao())

# Exercicio 15
def historia_interativa():
    escolha1 = input("Você está em uma floresta. Quer seguir para a 'esquerda' ou 'direita'? ").strip().lower()
    if escolha1 == "esquerda":
        escolha2 = input("Você encontra um lago. Quer 'nadar' ou 'andar' ao redor dele? ").strip().lower()
        if escolha2 == "nadar":
            return "Você nadou e encontrou uma ilha com um tesouro!"
        else:
            return "Você encontrou uma caverna escondida e achou um tesouro!"
    else:
        escolha2 = input("Você encontra um desfiladeiro. Quer 'pular' ou 'voltar'? ").strip().lower()
        if escolha2 == "pular":
            return "Você pulou com sucesso e encontrou um tesouro!"
        else:
            return "Você decidiu voltar e se perdeu na floresta..."

# Exemplo de uso:
print(historia_interativa())

# Exercicio 16
def verificar_paridade():
    numero = int(input("Digite um número: "))
    return "O número é par." if numero % 2 == 0 else "O número é ímpar."

# Exemplo de uso:
print(verificar_paridade())
