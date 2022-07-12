alunos = LOAD 'alunos.txt' USING PigStorage(',')
    as (id: chararray, nome: chararray, sobrenome: chararray, idade: int);
alunos_ordem = ORDER alunos BY idade;
Dump alunos_ordem;