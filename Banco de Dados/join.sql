-- INNER JOIN
-- Retorna valores que têm valores correspondentes nas duas tabelas
SELECT t.nome AS 'Nome do(a) pai/mãe', t2.nome AS  'Nome do(a) filho(a)' 
    FROM tabela t 
        INNER JOIN tabela2 t2 
            ON t.id = t2.id_heranca

-- LEFT JOIN
-- Retorna todos os valores da tabela da esquerda e os valores correspondentes da tabela da direita, se houver
SELECT t.nome AS 'Nome do(a) pai/mãe', t2.nome AS  'Nome do(a) filho(a)' 
    FROM tabela t 
        LEFT JOIN tabela2 t2 
            ON t.id = t2.id_heranca

-- RIGHT JOIN
-- Retorna todos os valores da tabela da direita e os valores correspondentes da tabela da esquerda, se houver
SELECT t.nome AS 'Nome do(a) pai/mãe', t2.nome AS  'Nome do(a) filho(a)' 
    FROM tabela t 
        RIGHT JOIN tabela2 t2 
            ON t.id = t2.id_heranca

-- CROSS JOIN
-- Retorna todos os valores das duas tabelas
SELECT t.nome AS 'Nome do(a) pai/mãe', t2.nome AS  'Nome do(a) filho(a)' 
    FROM tabela t 
        CROSS JOIN tabela2 t2 
            ON t.id = t2.id_heranca