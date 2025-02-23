class SistemaMedicamentos:
    def __init__(self):
        self.medicamentos = []
        self.carregar_dados_iniciais()

    def carregar_dados_iniciais(self):
        """Carrega os dados iniciais dos medicamentos do sistema"""
        disponibilidade_inicial = "Ozempic;201;15;1200.00#Victoza;202;10;700.00#Trulicity;203;50;800.00#Byetta;204;40;500.00#Bydureon;205;10;550.00#Rybelsus;206;8;600.00#Metformina;207;30;100.00#Jardiance;208;25;400.00#Farxiga;209;5;450.00#Invokana;210;3;400.00#Amaryl;211;12;150.00#Glifage;212;7;100.00"

        # Dividir a string pelos # e depois pelos ;
        for med in disponibilidade_inicial.split('#'):
            desc, cod, qtd, preco = med.split(';')
            self.medicamentos.append({
                'descricao': desc,
                'codigo': int(cod),
                'quantidade': int(qtd),
                'preco': float(preco)
            })

    def cadastrar_medicamento(self, descricao, codigo, quantidade, preco):
        """
        Cadastra um novo medicamento no sistema
        """
        # Verificar se código já existe
        if any(med['codigo'] == codigo for med in self.medicamentos):
            print("Erro: Código já existe!")
            return False

        novo_med = {
            'descricao': descricao,
            'codigo': codigo,
            'quantidade': quantidade,
            'preco': preco
        }
        self.medicamentos.append(novo_med)
        print("Medicamento cadastrado com sucesso!")
        return True

    def listar_medicamentos(self):
        """Mostra todos os medicamentos cadastrados"""
        print("\n" + "="*80)
        print("LISTA DE MEDICAMENTOS")
        print("="*80)
        for med in self.medicamentos:
            print(f"Código: {med['codigo']} | Descrição: {med['descricao'].ljust(20)} | "
                  f"Quantidade: {str(med['quantidade']).rjust(3)} | "
                  f"Preço: R$ {med['preco']:.2f}")
        print("="*80)

    def ordenar_por_quantidade(self, crescente=True):
        """Ordena medicamentos por quantidade"""
        self.medicamentos.sort(key=lambda x: x['quantidade'], reverse=not crescente)
        ordem = "crescente" if crescente else "decrescente"
        print(f"\nMedicamentos ordenados por quantidade em ordem {ordem}:")
        self.listar_medicamentos()

    def buscar_medicamento(self, **kwargs):
        """
        Busca medicamentos por descrição ou código
        Uso: buscar_medicamento(descricao="nome") ou buscar_medicamento(codigo=123)
        """
        resultados = []

        if 'descricao' in kwargs:
            desc = kwargs['descricao'].lower()
            resultados = [med for med in self.medicamentos
                         if desc in med['descricao'].lower()]
        elif 'codigo' in kwargs:
            cod = kwargs['codigo']
            resultados = [med for med in self.medicamentos
                         if med['codigo'] == cod]

        if not resultados:
            print("Nenhum medicamento encontrado!")
        else:
            print("\nMedicamentos encontrados:")
            for med in resultados:
                print(f"Código: {med['codigo']} - {med['descricao']} - "
                      f"Qtd: {med['quantidade']} - R$ {med['preco']:.2f}")

    def remover_medicamento(self, codigo):
        """Remove um medicamento pelo código"""
        for i, med in enumerate(self.medicamentos):
            if med['codigo'] == codigo:
                del self.medicamentos[i]
                print(f"Medicamento código {codigo} removido com sucesso!")
                return True
        print("Medicamento não encontrado!")
        return False

    def listar_esgotados(self):
        """Lista medicamentos com quantidade zero"""
        esgotados = [med for med in self.medicamentos if med['quantidade'] == 0]
        if esgotados:
            print("\nMedicamentos esgotados:")
            for med in esgotados:
                print(f"{med['descricao']} (Código: {med['codigo']})")
        else:
            print("Não há medicamentos esgotados!")

    def filtrar_baixa_quantidade(self, limite=5):
        """
        Lista medicamentos com quantidade abaixo do limite
        """
        baixo_estoque = [med for med in self.medicamentos if med['quantidade'] <= limite]
        if baixo_estoque:
            print(f"\nMedicamentos com quantidade abaixo de {limite}:")
            for med in baixo_estoque:
                print(f"{med['descricao']}: {med['quantidade']} unidades")
        else:
            print(f"Não há medicamentos abaixo do limite de {limite} unidades")

    def atualizar_quantidade(self, codigo, quantidade_delta):
        """
        Atualiza a quantidade de um medicamento
        quantidade_delta pode ser positivo (entrada) ou negativo (saída)
        """
        for med in self.medicamentos:
            if med['codigo'] == codigo:
                nova_qtd = med['quantidade'] + quantidade_delta
                if nova_qtd < 0:
                    print("Erro: Quantidade não pode ficar negativa!")
                    return False
                med['quantidade'] = nova_qtd
                print(f"Quantidade atualizada: {nova_qtd} unidades")
                return True
        print("Medicamento não encontrado!")
        return False

    def atualizar_preco(self, codigo, novo_preco):
        """Atualiza o preço de um medicamento"""
        for med in self.medicamentos:
            if med['codigo'] == codigo:
                if novo_preco < med['preco']:
                    print("Erro: Novo preço não pode ser menor que o atual!")
                    return False
                med['preco'] = novo_preco
                print("Preço atualizado com sucesso!")
                return True
        print("Medicamento não encontrado!")
        return False

    def calcular_valor_total(self):
        """Calcula valor total do estoque"""
        total = sum(med['quantidade'] * med['preco'] for med in self.medicamentos)
        print(f"\nValor total do estoque: R$ {total:.2f}")
        return total

    def calcular_lucro_presumido(self):
        """Calcula lucro presumido baseado nas regras de custo"""
        lucro_total = 0
        for med in self.medicamentos:
            # Define percentual de custo baseado no preço
            if med['preco'] <= 500:
                custo_percentual = 0.75  # 25% de custo
            elif med['preco'] <= 700:
                custo_percentual = 0.80  # 20% de custo
            else:
                custo_percentual = 0.85  # 15% de custo

            custo = med['preco'] * custo_percentual
            lucro_unit = med['preco'] - custo
            lucro_total += lucro_unit * med['quantidade']

        print(f"\nLucro presumido total: R$ {lucro_total:.2f}")
        return lucro_total

    def relatorio_geral(self):
        """Gera relatório geral dos medicamentos"""
        print("\n" + "="*90)
        print("RELATÓRIO GERAL DE MEDICAMENTOS".center(90))
        print("="*90)
        print("Código".ljust(8), "Descrição".ljust(20), "Quantidade".rjust(10),
              "Preço Unit.".rjust(15), "Valor Total".rjust(15))
        print("-"*90)

        total_geral = 0
        for med in self.medicamentos:
            valor_total = med['quantidade'] * med['preco']
            total_geral += valor_total
            print(
                f"{str(med['codigo']).ljust(8)}",
                f"{med['descricao'].ljust(20)}",
                f"{str(med['quantidade']).rjust(10)}",
                f"R$ {med['preco']:.2f}".rjust(15),
                f"R$ {valor_total:.2f}".rjust(15)
            )

        print("-"*90)
        print(f"Valor Total do Estoque: R$ {total_geral:.2f}".rjust(90))
        print("="*90)

def menu():
    """Exibe o menu principal do sistema"""
    sistema = SistemaMedicamentos()

    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE MEDICAMENTOS ===")
        print("1. Cadastrar medicamento")
        print("2. Listar medicamentos")
        print("3. Ordenar por quantidade")
        print("4. Buscar medicamento")
        print("5. Remover medicamento")
        print("6. Listar esgotados")
        print("7. Filtrar baixa quantidade")
        print("8. Atualizar quantidade")
        print("9. Atualizar preço")
        print("10. Calcular valor total")
        print("11. Calcular lucro presumido")
        print("12. Relatório geral")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '0':
            break
        elif opcao == '1':
            desc = input("Descrição: ")
            cod = int(input("Código: "))
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            sistema.cadastrar_medicamento(desc, cod, qtd, preco)
        elif opcao == '2':
            sistema.listar_medicamentos()
        elif opcao == '3':
            ordem = input("Ordem (c - crescente, d - decrescente): ").lower()
            sistema.ordenar_por_quantidade(ordem == 'c')
        elif opcao == '4':
            tipo = input("Buscar por (d - descrição, c - código): ").lower()
            if tipo == 'd':
                desc = input("Digite a descrição: ")
                sistema.buscar_medicamento(descricao=desc)
            else:
                cod = int(input("Digite o código: "))
                sistema.buscar_medicamento(codigo=cod)
        elif opcao == '5':
            cod = int(input("Código do medicamento a remover: "))
            sistema.remover_medicamento(cod)
        elif opcao == '6':
            sistema.listar_esgotados()
        elif opcao == '7':
            try:
                limite = int(input("Digite o limite (Enter para usar 5): "))
            except ValueError:
                limite = 5
            sistema.filtrar_baixa_quantidade(limite)
        elif opcao == '8':
            cod = int(input("Código do medicamento: "))
            qtd = int(input("Quantidade a adicionar (ou negativo para remover): "))
            sistema.atualizar_quantidade(cod, qtd)
        elif opcao == '9':
            cod = int(input("Código do medicamento: "))
            preco = float(input("Novo preço: "))
            sistema.atualizar_preco(cod, preco)
        elif opcao == '10':
            sistema.calcular_valor_total()
        elif opcao == '11':
            sistema.calcular_lucro_presumido()
        elif opcao == '12':
            sistema.relatorio_geral()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
