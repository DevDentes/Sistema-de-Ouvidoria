🧾 Objetivo do Projeto

O sistema de ouvidoria desenvolvido em Python tem como objetivo permitir o registro, consulta**** e remoção de manifestações feitas por usuários. Ele simula um sistema simples de atendimento público ou empresarial onde o cidadão ou cliente pode registrar reclamações, elogios, sugestões, etc.

🛠️ Tecnologias Utilizadas

Python: Linguagem de programação principal.

MySQL: Banco de dados relacional utilizado para armazenar as manifestações.

Biblioteca datetime: Para manipulação de datas.

Módulo personalizado operacoesbd: Contém funções para conexão e execução de comandos SQL no banco de dados.

📁 Funcionalidades Implementadas

O sistema é baseado em um menu com 6 opções principais:

Listar Manifestações

Exibe todas as manifestações cadastradas no banco de dados.

Cada manifestação mostra: código, tipo, descrição e data de criação.

Adicionar Manifestação

Permite ao usuário cadastrar uma nova manifestação.

Os dados são inseridos no banco com o tipo, descrição e a data atual.

Retorna o código da manifestação criada.

Pesquisar Manifestação

Busca uma manifestação específica a partir do seu código.

Exibe os detalhes se encontrado, ou uma mensagem de erro se o código for inválido.

Remover Manifestação

Exclui uma manifestação informando seu código.

Retorna uma mensagem de sucesso ou erro dependendo se o código existe ou não.

Sair

Encerra a execução do sistema.