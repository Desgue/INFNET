from datetime import datetime
import csv
import sqlite3

# ==================================================
# Funções de carregamento de dados
# ==================================================

def carregar_csv(nome):
    """Carrega dados de um arquivo CSV para memória"""
    with open(nome, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def carregar_dados_sql(cursor):
    """Carrega dados para o banco SQLite"""
    tabelas = {
        'Cargos': 'cargos.csv',
        'Departamentos': 'departamentos.csv',
        'Funcionarios': 'funcionarios.csv',
        'HistoricoSalarios': 'historicoSalarios.csv',
        'Dependentes': 'dependentes.csv'
    }

    for tabela, arquivo in tabelas.items():
        dados = carregar_csv(arquivo)
        if dados:
            cols = dados[0].keys()
            placeholders = ','.join(['?'] * len(cols))
            cursor.executemany(
                f'INSERT INTO {tabela} ({",".join(cols)}) VALUES ({placeholders})',
                [tuple(item.values()) for item in dados]
            )

def criar_banco_dados():
    """Cria e popula o banco de dados SQLite"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    # Criação das tabelas
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Cargos (
        codigo INT PRIMARY KEY,
        descricao TEXT NOT NULL,
        salario_base REAL NOT NULL,
        nivel TEXT NOT NULL CHECK(nivel IN ('estagiário', 'técnico', 'analista', 'gerente', 'diretor')),
        beneficios TEXT
    );

    CREATE TABLE IF NOT EXISTS Departamentos (
        codigo INT PRIMARY KEY,
        nome TEXT NOT NULL,
        cod_gerente INT,
        andar INT NOT NULL,
        telefone TEXT,
        FOREIGN KEY (cod_gerente) REFERENCES Funcionarios(codigo)
    );

    CREATE TABLE IF NOT EXISTS Funcionarios (
        codigo INT PRIMARY KEY,
        nome TEXT NOT NULL,
        cod_cargo INT NOT NULL,
        cod_departamento INT NOT NULL,
        salario REAL NOT NULL,
        data_admissao TEXT NOT NULL,
        FOREIGN KEY (cod_cargo) REFERENCES Cargos(codigo),
        FOREIGN KEY (cod_departamento) REFERENCES Departamentos(codigo)
    );

    CREATE TABLE IF NOT EXISTS HistoricoSalarios (
        mes_ano TEXT,
        salario REAL,
        cod_funcionario INT,
        FOREIGN KEY (cod_funcionario) REFERENCES Funcionarios(codigo)
    );

    CREATE TABLE IF NOT EXISTS Dependentes (
        nome TEXT,
        parentesco TEXT,
        data_nascimento TEXT,
        cod_funcionario INT,
        FOREIGN KEY (cod_funcionario) REFERENCES Funcionarios(codigo)
    );
    ''')

    # Popula o banco de dados
    carregar_dados_sql(cursor)
    conn.commit()
    conn.close()

# ==================================================
# Consultas SQL (1, 2, 5, 6, 8)
# ==================================================

def consulta1_listar_tabelas():
    """1. Listar tabelas ordenadas"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    tabelas = ['Cargos', 'Departamentos', 'Funcionarios', 'HistoricoSalarios', 'Dependentes']
    for tabela in tabelas:
        cursor.execute(f'SELECT * FROM {tabela}')
        print(f"\n{tabela}:")
        for linha in cursor.fetchall():
            print(linha)

    conn.close()

def consulta2_funcionarios_detalhes():
    """2. Listar funcionários com detalhes"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT F.nome, C.descricao, D.nome, GROUP_CONCAT(DP.nome, ', ')
    FROM Funcionarios F
    JOIN Cargos C ON F.cod_cargo = C.codigo
    JOIN Departamentos D ON F.cod_departamento = D.codigo
    LEFT JOIN Dependentes DP ON F.codigo = DP.cod_funcionario
    GROUP BY F.codigo
    ''')

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def consulta5_estagiarios_filhos():
    """5. Listar estagiários com filhos"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT F.nome, DP.nome, DP.parentesco
    FROM Funcionarios F
    JOIN Cargos C ON F.cod_cargo = C.codigo
    JOIN Dependentes DP ON F.codigo = DP.cod_funcionario
    WHERE C.nivel = 'estagiário' AND DP.parentesco LIKE 'filh%'
    ''')

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def consulta6_salario_medio_alto():
    """6. Funcionário com maior salário médio"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT F.nome, AVG(H.salario)
    FROM Funcionarios F
    JOIN HistoricoSalarios H ON F.codigo = H.cod_funcionario
    GROUP BY F.codigo
    ORDER BY AVG(H.salario) DESC
    LIMIT 1
    ''')

    print(cursor.fetchone())
    conn.close()

def consulta8_analista_salario_alto():
    """8. Analista com melhor salário na faixa"""
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT F.nome, F.salario
    FROM Funcionarios F
    JOIN Cargos C ON F.cod_cargo = C.codigo
    WHERE C.nivel = 'analista' AND F.salario BETWEEN 5000 AND 9000
    ORDER BY F.salario DESC
    LIMIT 1
    ''')

    print(cursor.fetchone())
    conn.close()

# ==================================================
# Consultas Python (3, 4, 7, 9, 10)
# ==================================================

def consulta3_aumento_salarial():
    """3. Funcionários com aumento nos últimos 3 meses"""
    funcionarios = carregar_csv('funcionarios.csv')
    historico = carregar_csv('historicoSalarios.csv')

    aumentos = []
    for func in funcionarios:
        cod = func['codigo']
        salarios = [float(h['salario']) for h in historico if h['cod_funcionario'] == cod][-3:]
        if len(salarios) > 1 and any(salarios[i] > salarios[i-1] for i in range(1, len(salarios))):
            aumentos.append(func['nome'])
    return aumentos

def consulta4_media_idade_filhos():
    """4. Média de idade dos filhos por departamento"""
    dependentes = carregar_csv('dependentes.csv')
    funcionarios = carregar_csv('funcionarios.csv')
    departamentos = carregar_csv('departamentos.csv')

    idades = {}
    for dep in dependentes:
        if dep['parentesco'] not in ['filho', 'filha']: continue

        data_nasc = datetime.strptime(dep['data_nascimento'], '%Y-%m-%d')
        idade = datetime.now().year - data_nasc.year

        func = next(f for f in funcionarios if f['codigo'] == dep['cod_funcionario'])
        dept = next(d for d in departamentos if d['codigo'] == func['cod_departamento'])

        idades.setdefault(dept['nome'], []).append(idade)

    return {dept: sum(vals)/len(vals) for dept, vals in idades.items()}

def consulta7_analistas_duas_filhas():
    """7. Analistas com duas filhas"""
    funcionarios = carregar_csv('Funcionarios.csv')
    cargos = carregar_csv('Cargos.csv')
    dependentes = carregar_csv('Dependentes.csv')

    analistas = [
        f for f in funcionarios
        if next(c for c in cargos if c['codigo'] == f['cod_cargo'])['nivel'] == 'analista'
    ]

    return [
        a['nome'] for a in analistas
        if len([d for d in dependentes
              if d['cod_funcionario'] == a['codigo'] and d['parentesco'] == 'filha']) == 2
    ]

def consulta9_departamento_mais_dependentes():
    """9. Departamento com mais dependentes"""
    dependentes = carregar_csv('dependentes.csv')
    funcionarios = carregar_csv('funcionarios.csv')
    departamentos = carregar_csv('departamentos.csv')

    contagem = {}
    for d in dependentes:
        func = next(f for f in funcionarios if f['codigo'] == d['cod_funcionario'])
        dept = next(dep for dep in departamentos if dep['codigo'] == func['cod_departamento'])
        contagem[dept['nome']] = contagem.get(dept['nome'], 0) + 1

    return max(contagem.items(), key=lambda x: x[1])

def consulta10_media_salarial_departamento():
    """10. Média salarial por departamento"""
    funcionarios = carregar_csv('Funcionarios.csv')
    departamentos = carregar_csv('Departamentos.csv')

    medias = {}
    for func in funcionarios:
        dept = next(d for d in departamentos if d['codigo'] == func['cod_departamento'])
        medias.setdefault(dept['nome'], []).append(float(func['salario']))

    return sorted(
        [(dept, sum(vals)/len(vals)) for dept, vals in medias.items()],
        key=lambda x: x[1],
        reverse=True
    )

# ==================================================
# Função main (em branco para futuras expansões)
# ==================================================

def main():
    # Garante a criação do banco de dados antes de executar as consultas
    criar_banco_dados()

    # Exemplo de uso das consultas
    print("=== Consulta 1 ===")
    consulta1_listar_tabelas()

    print("\n=== Consulta 2 ===")
    consulta2_funcionarios_detalhes()

    print("\n=== Consulta 3 ===")
    print(consulta3_aumento_salarial())

    print("\n=== Consulta 4 ===")
    for dept, media in consulta4_media_idade_filhos().items():
        print(f"{dept}: {media:.1f} anos")

    print("\n=== Consulta 5 ===")
    consulta5_estagiarios_filhos()

    print("\n=== Consulta 6 ===")
    consulta6_salario_medio_alto()

    print("\n=== Consulta 7 ===")
    print(consulta7_analistas_duas_filhas())

    print("\n=== Consulta 8 ===")
    consulta8_analista_salario_alto()

    print("\n=== Consulta 9 ===")
    dept, total = consulta9_departamento_mais_dependentes()
    print(f"{dept} ({total} dependentes)")

    print("\n=== Consulta 10 ===")
    for dept, media in consulta10_media_salarial_departamento():
        print(f"{dept}: R${media:.2f}")

if __name__ == "__main__":
    main()
