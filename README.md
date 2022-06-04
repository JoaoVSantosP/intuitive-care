# Teste processo seletivo IntuitiveCare BackEnd

# [TESTE 1 - WebScraping]

## Tarefas de código:
* 1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude
* 1.2 - Baixar os Anexos I ao Anexo IV
* 1.3 - Agrupar os anexos em um mesmo arquivo compactado (ZIP, RAR, ...)


# [TESTE 2 - Transformação de dados] 
### Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse e-mail) que execute as tarefas de código abaixo.

## Tarefas de código
* Extrair do pdf do anexo I do teste 1 acima os dados da tabela Rol de Procedimentos e Eventos em Saúde (todas as páginas);
* Salvar dados em uma tabela estruturada, em csv;
* Zipar o csv num arquivo "Teste_{seu_nome}.zip".


# [TESTE 3 - Banco de dados] 
### Neste teste o candidato deverá criar scripts .sql (MySQL 8. ou Postgres >10.0) que execute as tarefas de código abaixo.

## Tarefas de preparação
* Baixar os arquivos dos últimos 2 anos no repositório público: http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

## Tarefas de código
* Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.
* Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação. Atenção ao encoding dos arquivos no momento da importação!
* Montar uma query analítica que traga a resposta para as seguintes perguntas:

Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?

# [TESTE 4 - API] 
### Neste teste o candidato deverá criar uma interface web (usando o framework Vue.js) que se comunicará com um servidor em uma das linguagens mencionadas no fim desse email para realizar as tarefas de código abaixo.

## Tarefas de código
* Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham
* Criar coleção no Postman para exibir resultado
