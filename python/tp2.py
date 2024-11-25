# Exercicio 1 - Validação de Senha
def validar_senha():
    senha = input("Digite sua senha: ")
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    
    if len(senha) >= 6 and tem_maiuscula and tem_numero:
        print("Senha forte!")
    else:
        print("Senha fraca! Requisitos:")
        if len(senha) < 6: print("- Mínimo 6 caracteres")
        if not tem_maiuscula: print("- Uma letra maiúscula")
        if not tem_numero: print("- Um número")

# Exercicio 2 - Contagem de Números Ímpares
def contar_impares():
    num = int(input("Digite um número: "))
    impares = len([x for x in range(1, num + 1) if x % 2 != 0])
    print(f"Existem {impares} números ímpares até {num}")

# Exercicio 3 - Soma de Números Pares
def soma_pares():
    num = int(input("Digite um número: "))
    soma = sum(x for x in range(2, num + 1, 2))
    print(f"A soma dos números pares até {num} é {soma}")

# Exercicio 4 - Lista de Números Positivos com While
def listar_positivos():
    num = int(input("Digite um número: "))
    i = 1
    while i <= num:
        print(i, end=" ")
        i += 1

# Exercicio 5 - Contagem Regressiva
def contagem_regressiva():
    num = int(input("Digite um número: "))
    while num >= 0:
        print(num, end=" ")
        num -= 1

# Exercicio 6 - Média de Notas
def media_notas():
    notas = []
    while True:
        nota = float(input("Digite uma nota (negativa para sair): "))
        if nota < 0: break
        notas.append(nota)
    print(f"Média: {sum(notas)/len(notas):.2f}")

# Exercicio 7 - Números Pares com Loop For
def pares_for():
    for i in range(0, 11, 2):
        print(i, end=" ")

# Exercicio 8 - Função de Cálculo da Média das Maiores Notas
def calcular_media(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]
    return sum(sorted(notas)[1:]) / 2

# Exercicio 9 - Saudação Personalizada
def saudacao(nome):
    print(f"Acerehe ha merre {nome}! Vamos dançar o ragatanga? ")

# Exercicio 10 - Série de Fibonacci
def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b

# Exercicio 11 - Função de Potência
def super_potencia(base, expoente):
    return base ** expoente

# Exercicio 12 - Contagem de Palavras em uma Frase
def contar_palavras(frase):
    return len(frase.split())

# Exercicio 13 - Números Primos com While
def numeros_primos():
    def eh_primo(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False
        return True
    
    count, num = 0, 2
    while count < 10:
        if eh_primo(num):
            print(num, end=" ")
            count += 1
        num += 1

# Exercicio 14 - Impressão de Tabuada
def imprimir_tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Exercicio 15 - Agenda de Contatos
def agenda_contatos():
    contatos = {}
    for _ in range(3):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        contatos[nome] = telefone
    
    print("\nLista de Contatos:")
    for nome, tel in contatos.items():
        print(f"{nome}: {tel}")

# Exercicio 16 - Criação e Correção de Prova Objetiva
def prova_objetiva():
    prova = {}
    print("Cadastro da prova:")
    for i in range(3):
        pergunta = input(f"Digite a pergunta {i+1}: ")
        resposta = input(f"Digite a resposta correta: ")
        prova[pergunta] = resposta
    
    print("\nResponda a prova:")
    acertos = 0
    for pergunta, resposta_correta in prova.items():
        resposta_aluno = input(f"{pergunta}\nResposta: ")
        if resposta_aluno.lower() == resposta_correta.lower():
            acertos += 1
    
    print(f"\nVocê acertou {acertos} de 3 questões")

# Menu principal para testar as funções
def menu():
    while True:
        print("\nEscolha um exercício (0 para sair):")
        for i in range(1, 17):
            print(f"{i} - Exercício {i}")
        try:
            opcao = int(input("Opção: "))
        except:
            print("\nOpção Inválida\nEscolha um número de 1-16")
            continue
        if opcao == 0:
            break
        
        funcoes = {
            1: validar_senha,
            2: contar_impares,
            3: soma_pares,
            4: listar_positivos,
            5: contagem_regressiva,
            6: media_notas,
            7: pares_for,
            8: lambda: print(calcular_media(7, 8, 9)),
            9: lambda: saudacao("Meu xará"),
            10: fibonacci,
            11: lambda: print(super_potencia(2, 3)),
            12: lambda: print(contar_palavras("Tres pratos de trigo para tres tigres tristes")),
            13: numeros_primos,
            14: lambda: imprimir_tabuada(42),
            15: agenda_contatos,
            16: prova_objetiva
        }
        
        if opcao in funcoes:
            funcoes[opcao]()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()