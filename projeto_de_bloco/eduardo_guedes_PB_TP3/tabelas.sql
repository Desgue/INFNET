CREATE TABLE Cargos (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    salario_base REAL NOT NULL,
    nivel VARCHAR(50) NOT NULL CHECK (nivel IN ('estagiário', 'técnico', 'analista', 'gerente', 'diretor')),
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
    FOREIGN KEY (cod_cargo) REFERENCES Cargos(codigo),
    FOREIGN KEY (cod_departamento) REFERENCES Departamentos(codigo)
);

ALTER TABLE Departamentos
ADD CONSTRAINT fk_gerente
FOREIGN KEY (cod_gerente) REFERENCES Funcionarios(codigo);
