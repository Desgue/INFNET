# TP1 - Projeto de Banco de Dados Relacional

## 1. Tipos de Relacionamentos

Existem três tipos principais de relacionamentos:

1. **Um para Um (1:1)**: Cada registro em uma tabela está relacionado a apenas um registro em outra tabela.
   Exemplo: Um cliente possui um único CPF, e um CPF pertence a um único cliente.

2. **Um para Muitos (1:N)**: Um registro em uma tabela pode estar relacionado a vários registros em outra tabela.
   Exemplo: Um departamento pode ter vários funcionários, mas cada funcionário pertence a apenas um departamento.

3. **Muitos para Muitos (N:N)**: Vários registros em uma tabela podem estar relacionados a vários registros em outra tabela.
   Exemplo: Um aluno pode estar matriculado em várias disciplinas, e cada disciplina pode ter vários alunos.

## 2. Valores NULL

O valor NULL representa a ausência de valor em um campo. Isso pode significar:
- Valor desconhecido
- Valor não aplicável
- Valor não informado

Problemas decorrentes do uso de NULL:
- Complexidade em consultas (necessidade de tratamento especial)
- Ambiguidade na interpretação dos dados
- Ocupação de espaço extra no banco de dados
- Comportamento especial em operações de comparação

## 3. Campo UNIQUE

Um campo UNIQUE garante que não existam valores duplicados naquela coluna da tabela.

Exemplo: O campo email em uma tabela de usuários deve ser UNIQUE, pois não podem existir dois usuários com o mesmo email.

## 4. Chave Primária

A chave primária é um campo ou conjunto de campos que identifica de forma única cada registro em uma tabela.

Exemplo: Em uma tabela de funcionários, o número de matrícula é a chave primária, pois cada funcionário tem um número único.

## 5. Criação do Banco e Tabela

```sql
--- Criação do Banco de Dados
CREATE DATABASE agenda;

-- Criação da tabela contatos
CREATE TABLE contatos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE
);

```

## 6. Inserção com ID Duplicado

Teste de inserção com ID duplicado:
```sql
-- Primeira inserção
INSERT INTO contatos (id, nome, telefone) VALUES (1, 'João', '1234-5678');

-- Segunda inserção com mesmo ID (irá gerar erro)
INSERT INTO contatos (id, nome, telefone) VALUES (1, 'Maria', '8765-4321');
```

O resultado será um erro de violação de chave primária (UNIQUE constraint failed: contatos.id)

## 7. Inserção com Nome Nulo

Teste de inserção com nome nulo:
```sql
-- Tentativa de inserção com nome NULL
INSERT INTO contatos (id, nome, telefone) VALUES (2, NULL, '9999-9999');
```

O resultado será um erro de violação de NOT NULL (NOT NULL constraint failed: contatos.nome)

## 8. Inserção com Telefone Duplicado

Teste de inserção com telefone duplicado:
```sql
-- Primeira inserção
INSERT INTO contatos (id, nome, telefone) VALUES (2, 'Maria', '1234-5678');

-- Segunda inserção com mesmo telefone (irá gerar erro)
INSERT INTO contatos (id, nome, telefone) VALUES (3, 'José', '1234-5678');
```

O resultado será um erro de violação de UNIQUE (UNIQUE constraint failed: contatos.telefone)

## 9. Exibição dos Registros

Para exibir todos os registros:
```sql
SELECT * FROM contatos;
```

## 10. Chave Estrangeira

Uma chave estrangeira é um campo que estabelece um relacionamento com a chave primária de outra tabela.

Exemplo: Em uma tabela de pedidos, o campo id_cliente é uma chave estrangeira que referencia a tabela de clientes, estabelecendo uma relação entre o pedido e o cliente que o realizou.

## 11. Criação da Tabela de Endereços

```sql
CREATE TABLE enderecos (
    id INTEGER PRIMARY KEY,
    rua TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT,
    id_contato INTEGER UNIQUE,
    FOREIGN KEY (id_contato) REFERENCES contatos(id)
);
```

## 12. Inserção com ID de Contato Duplicado

Teste de inserção com ID de contato duplicado:
```sql
-- Primeira inserção
INSERT INTO enderecos (id, rua, id_contato) VALUES (1, 'Rua A', 1);

-- Segunda inserção com mesmo id_contato (irá gerar erro)
INSERT INTO enderecos (id, rua, id_contato) VALUES (2, 'Rua B', 1);
```

O resultado será um erro de violação de UNIQUE (UNIQUE constraint failed: enderecos.id_contato)

## 13. Chave Estrangeira sem UNIQUE

Se a chave estrangeira id_contato não fosse UNIQUE, isso significaria que um contato poderia ter múltiplos endereços, mudando o relacionamento de 1:1 para 1:N. Neste caso:
- Um contato poderia ter vários endereços registrados
- Seria possível cadastrar diferentes endereços para o mesmo contato
- O relacionamento seria do tipo "um para muitos" em vez de "um para um"

## 14. Exibição dos Endereços

Para exibir todos os endereços:
```sql
SELECT * FROM enderecos;
```

## 15. Sistema Acadêmico

### Modelo Lógico:

```sql
-- Tabela de alunos
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

-- Tabela de endereços (1:1 com alunos)
CREATE TABLE enderecos (
    id INTEGER PRIMARY KEY,
    id_aluno INTEGER UNIQUE,
    rua TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id)
);

-- Tabela de emails (1:N com alunos)
CREATE TABLE emails (
    id INTEGER PRIMARY KEY,
    id_aluno INTEGER,
    email TEXT UNIQUE,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id)
);

-- Tabela de telefones (1:N com alunos)
CREATE TABLE telefones (
    id INTEGER PRIMARY KEY,
    id_aluno INTEGER,
    telefone TEXT UNIQUE,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id)
);

-- Tabela de disciplinas
CREATE TABLE disciplinas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

-- Tabela de relacionamento entre alunos e disciplinas (N:N)
CREATE TABLE matriculas (
    id_aluno INTEGER,
    id_disciplina INTEGER,
    data_matricula DATE,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
);
```

## 16. Sistema Bancário

### Modelo Lógico:

```sql
-- Tabela de agências
CREATE TABLE agencias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    numero TEXT UNIQUE,
    endereco TEXT
);

-- Tabela de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    data_cadastro DATE
);

-- Tabela de contas
CREATE TABLE contas (
    id INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_agencia INTEGER,
    numero TEXT UNIQUE,
    tipo TEXT,
    saldo DECIMAL(10,2),
    data_abertura DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_agencia) REFERENCES agencias(id)
);

-- Tabela de transações
CREATE TABLE transacoes (
    id INTEGER PRIMARY KEY,
    id_conta INTEGER,
    tipo TEXT,
    valor DECIMAL(10,2),
    data_hora DATETIME,
    descricao TEXT,
    FOREIGN KEY (id_conta) REFERENCES contas(id)
);
```

Para os modelos conceituais das questões 15 e 16, seria necessário usar uma ferramenta de modelagem como draw.io ou MySQL Workbench para criar os diagramas entidade-relacionamento (DER).
