CREATE TABLE Cargos (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    salario_base REAL NOT NULL,
    nivel VARCHAR(50) NOT NULL CHECK (
        nivel IN (
            'estagiário',
            'técnico',
            'analista',
            'gerente',
            'diretor'
        )
    ),
    beneficios TEXT
);

CREATE TABLE Departamentos (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cod_gerente INT,
    andar INT NOT NULL,
    telefone VARCHAR(15)
);

CREATE TABLE Funcionarios (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cod_cargo INT NOT NULL,
    cod_departamento INT NOT NULL,
    salario REAL NOT NULL,
    data_admissao DATE NOT NULL,
    FOREIGN KEY (cod_cargo) REFERENCES Cargos (codigo),
    FOREIGN KEY (cod_departamento) REFERENCES Departamentos (codigo)
);

CREATE TABLE Projetos (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_conclusao DATE,
    cod_funcionario INT NOT NULL,
    custo_previsto REAL NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (
        status IN (
            'Em Planejamento',
            'Em Execução',
            'Concluído',
            'Cancelado'
        )
    ),
    prioridade VARCHAR(20) DEFAULT 'Média',
    departamento_responsavel INT,
    FOREIGN KEY (cod_funcionario) REFERENCES Funcionarios (codigo),
    FOREIGN KEY (departamento_responsavel) REFERENCES Departamentos (codigo)
);

CREATE TABLE RecursosProjeto (
    codigo INT PRIMARY KEY,
    cod_projeto INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    tipo_recurso VARCHAR(20) NOT NULL CHECK (
        tipo_recurso IN ('financeiro', 'material', 'humano')
    ),
    quantidade REAL NOT NULL,
    unidade_medida VARCHAR(20),
    data_utilizacao DATE NOT NULL,
    custo_unitario REAL,
    observacoes TEXT,
    FOREIGN KEY (cod_projeto) REFERENCES Projetos (codigo)
);

ALTER TABLE Departamentos ADD CONSTRAINT fk_gerente FOREIGN KEY (cod_gerente) REFERENCES Funcionarios (codigo);
