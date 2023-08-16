CREATE TABLE usuarios (
    id_usu        INTEGER   PRIMARY KEY NOT NULL,
    nome_usu      TEXT (50) NOT NULL,
    username_usu  TEXT (15) NOT NULL,
    senha_usu     TEXT (8) NOT NULL,
    pontuacao_usu INTEGER
);

CREATE TABLE trofeus (
    id_tro   INTEGER   PRIMARY KEY NOT NULL,
    nome_tro TEXT (50) UNIQUE NOT NULL
);

CREATE TABLE colecoes (
    id_usu   INTEGER   REFERENCES usuarios (id_usu) ON DELETE CASCADE
                                                    ON UPDATE CASCADE
                                                    MATCH SIMPLE
                       NOT NULL,
    id_tro   INTEGER   REFERENCES trofeus (id_tro) ON DELETE CASCADE
                                                   ON UPDATE CASCADE
                                                   MATCH SIMPLE
                       NOT NULL,
    data_col TEXT (10) 
);

CREATE TABLE Livros (
    id_liv          INTEGER   PRIMARY KEY
                              NOT NULL,
    titulo_liv      TEXT (50) NOT NULL,
    autor_liv       TEXT (50) NOT NULL,
    totalpagina_liv INTEGER   NOT NULL,
    estili_liv      TEXT (25) NOT NULL
);

CREATE TABLE Leituras (
    id_usu   INTEGER   REFERENCES usuarios (id_usu) ON DELETE CASCADE
                                                    ON UPDATE CASCADE
                                                    MATCH SIMPLE
                       NOT NULL,
    id_liv   INTEGER   REFERENCES livros (id_liv) ON DELETE CASCADE
                                                   ON UPDATE CASCADE
                                                   MATCH SIMPLE
                       NOT NULL,
    lido_leitura INTEGER(1) NOT NULL
);


INSERT INTO usuarios (
                         id_usu,
                         nome_usu,
                         username_usu,
                         senha_usu
                     )
                     VALUES (
                         1,
                         'João da Silva',
                         'joao.silva',
                         'senha123'
                     );
                     
INSERT INTO usuarios (
                         id_usu,
                         nome_usu,
                         username_usu,
                         senha_usu
                     )
                     VALUES (
                         2,
                         'Maria Oliveira',
                         'maria.oliveira',
                         'segredo456'
                     );		
INSERT INTO usuarios (
                         id_usu,
                         nome_usu,
                         username_usu,
                         senha_usu
                     )
                     VALUES (
                         3,
                         'Pedro Santos',
                         'pedro.santos',
                         '123456789'
                     );		
INSERT INTO usuarios (
                         id_usu,
                         nome_usu,
                         username_usu,
                         senha_usu
                     )
                     VALUES (
                         4,
                         'Ana Rodrigues',
                         'ana_r',
                         'minhasenha'
                     );		

INSERT INTO usuarios (
                         id_usu,
                         nome_usu,
                         username_usu,
                         senha_usu
                     )
                     VALUES (
                         5,
                         'Luís Pereira',
                         'luis123',
                         'senha321'
                     );