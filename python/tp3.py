# exercicio 1
def dividir_string(texto):
    meio = len(texto) // 2
    return [texto[:meio], texto[meio:]]

# exercicio 2
def verificar_prefixo(texto, prefixo):
    return texto.startswith(prefixo)

# exercicio 3
def string_para_lista(texto):
    return list(texto)

# exercicio 4
def substitui_str(texto, antiga, nova):
    return texto.replace(antiga, nova)

# exercicio 5
def apenas_digitos(texto):
    return texto.isdigit()

# exercicio 6
def inverter_numero(numero):
    return str(numero)[::-1]

# exercicio 7
def traduzir_numeros(texto):
    numeros = {
        '0': 'zero', '1': 'um', '2': 'dois', '3': 'três',
        '4': 'quatro', '5': 'cinco', '6': 'seis',
        '7': 'sete', '8': 'oito', '9': 'nove'
    }
    resultado = ''
    for digito in texto:
        resultado += numeros.get(digito, digito) + ' '
    return resultado.strip()

# exercicio 8
def remover_duplicados(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

# exercicio 9
def soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

# exercicio 10
def caracteres_comuns(texto1, texto2):
    comuns = []
    for char in texto1:
        if char in texto2 and char not in comuns:
            comuns.append(char)
    return comuns

# exercicio 11
def inserir_palavra(lista_palavras, nova_palavra):
    if len(lista_palavras) < 3:
        lista_palavras.append(nova_palavra)
    else:
        posicao = int(input("Digite a posição para inserir a palavra: "))
        lista_palavras.insert(posicao, nova_palavra)
    return lista_palavras

# exercicio 12
def combinar_listas(lista1, lista2):
    lista_combinada = lista1.copy()
    lista_combinada.extend(lista2)
    return lista_combinada

# exercicio 13
def apagar_duplicatas(lista_palavras):
    return remover_duplicados(lista_palavras)

# exercicio 14
def organizar_compras(lista_compras):
    if not lista_compras:
        print("Não há mais itens para remover")
        return lista_compras
    
    lista_compras.pop()
    return lista_compras

# exercicio 15
def manusear_string(texto):
    print(f"String original: {texto}")
    inicio = int(input("Digite o índice de início: "))
    fim = int(input("Digite o índice de fim: "))
    return texto[inicio:fim]

# exercicio 16
def administrar_lista_compras(lista_compras):
    while True:
        comando = input("Digite um comando:\n\tfim: para terminar o programa\n\tretirar <nome do item>: para remover um item da lista\n\tacrescentar <indice> <produto>: para adicionar um produto na posicao indicada)\n> ")
        
        if comando == "fim":
            break
            
        elif comando.startswith("retirar"):
            item = comando.split(maxsplit=1)[1]
            try:
                indice = int(item)
                lista_compras.pop(indice)
            except ValueError:
                if item in lista_compras:
                    lista_compras.remove(item)
                    
        elif comando.startswith("acrescentar"):
            _, indice, *nome_produto = comando.split()
            lista_compras.insert(int(indice), " ".join(nome_produto))
    
    return lista_compras

def testar_funcoes():
    while True:
        print("\nEscolha uma função para testar (1-16) ou 0 para sair:")
        print("1. Dividir string em duas metades")
        print("2. Verificar prefixo")
        print("3. Converter string para lista")
        print("4. Substituir substring")
        print("5. Verificar se string contém apenas dígitos")
        print("6. Inverter número")
        print("7. Traduzir números para português")
        print("8. Remover duplicatas de lista")
        print("9. Soma dos dígitos")
        print("10. Caracteres comuns entre strings")
        print("11. Inserir palavra em lista")
        print("12. Combinar listas")
        print("13. Apagar duplicatas")
        print("14. Organizar compras")
        print("15. Manusear string")
        print("16. Administrar lista de compras")
        
        try:
            opcao = int(input("\nDigite o número da função (0 para sair): "))
            
            if opcao == 0:
                print("Encerrando o programa...")
                break
                
            if opcao < 1 or opcao > 16:
                print("Opção inválida. Escolha um número entre 1 e 16.")
                continue
                
            # Testes específicos para cada função
            if opcao == 1:
                texto = input("Digite uma string para dividir: ")
                resultado = dividir_string(texto)
                print(f"Resultado: {resultado}")
                
            elif opcao == 2:
                texto = input("Digite o texto: ")
                prefixo = input("Digite o prefixo: ")
                resultado = verificar_prefixo(texto, prefixo)
                print(f"Resultado: {resultado}")
                
            elif opcao == 3:
                texto = input("Digite uma string para converter em lista: ")
                resultado = string_para_lista(texto)
                print(f"Resultado: {resultado}")
                
            elif opcao == 4:
                texto = input("Digite o texto original: ")
                antiga = input("Digite a substring a ser substituída: ")
                nova = input("Digite a nova substring: ")
                resultado = substitui_str(texto, antiga, nova)
                print(f"Resultado: {resultado}")
                
            elif opcao == 5:
                texto = input("Digite uma string para verificar se contém apenas dígitos: ")
                resultado = apenas_digitos(texto)
                print(f"Resultado: {resultado}")
                
            elif opcao == 6:
                numero = int(input("Digite um número para inverter: "))
                resultado = inverter_numero(numero)
                print(f"Resultado: {resultado}")
                
            elif opcao == 7:
                texto = input("Digite uma string contendo números (0-9): ")
                resultado = traduzir_numeros(texto)
                print(f"Resultado: {resultado}")
                
            elif opcao == 8:
                lista = input("Digite elementos da lista separados por espaço: ").split()
                resultado = remover_duplicados(lista)
                print(f"Resultado: {resultado}")
                
            elif opcao == 9:
                numero = int(input("Digite um número para somar seus dígitos: "))
                resultado = soma_digitos(numero)
                print(f"Resultado: {resultado}")
                
            elif opcao == 10:
                texto1 = input("Digite a primeira string: ")
                texto2 = input("Digite a segunda string: ")
                resultado = caracteres_comuns(texto1, texto2)
                print(f"Resultado: {resultado}")
                
            elif opcao == 11:
                lista = input("Digite elementos da lista separados por espaço: ").split()
                nova_palavra = input("Digite a nova palavra: ")
                resultado = inserir_palavra(lista, nova_palavra)
                print(f"Resultado: {resultado}")
                
            elif opcao == 12:
                lista1 = input("Digite elementos da primeira lista separados por espaço: ").split()
                lista2 = input("Digite elementos da segunda lista separados por espaço: ").split()
                resultado = combinar_listas(lista1, lista2)
                print(f"Resultado: {resultado}")
                
            elif opcao == 13:
                lista = input("Digite elementos da lista separados por espaço: ").split()
                resultado = apagar_duplicatas(lista)
                print(f"Resultado: {resultado}")
                
            elif opcao == 14:
                lista = input("Digite itens da lista de compras separados por espaço: ").split()
                resultado = organizar_compras(lista)
                print(f"Resultado: {resultado}")
                
            elif opcao == 15:
                texto = input("Digite uma string para manusear: ")
                resultado = manusear_string(texto)
                print(f"Resultado: {resultado}")
                
            elif opcao == 16:
                lista = input("Digite itens da lista de compras separados por espaço: ").split()
                resultado = administrar_lista_compras(lista)
                print(f"Resultado final: {resultado}")
                
        except ValueError:
            print("Erro: Digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    testar_funcoes()