# -ETL_Python
Trilha Python Bootcamp Santander

# Descrição Detalhada do Código

## Introdução
Este código Python é um programa simples que avalia a elegibilidade dos clientes para empréstimos ou oportunidades de investimento com base em seus saldos de conta e limites de cartão de crédito. Ele também atualiza os objetos de cliente com uma chave chamada "elegibilidade" que possui valores 0 ou 1 para indicar a elegibilidade. Além disso, gera mensagens de marketing personalizadas para cada cliente com base em sua elegibilidade.

## Dados dos Clientes
O código começa com uma lista chamada "clientes", que contém informações fictícias de cinco clientes. Cada cliente é representado como um dicionário contendo "id", "name", informações de "account" (conta bancária) e informações de "card" (cartão de crédito).

## Determinação de Elegibilidade
A função `determinar_elegibilidade` é usada para determinar a elegibilidade de cada cliente. Ela compara o limite da conta bancária com o limite do cartão de crédito. Se o limite da conta for menor que o limite do cartão, o cliente é considerado elegível para um empréstimo (e a chave "elegibilidade" recebe o valor 1). Caso contrário, o cliente é elegível para uma oportunidade de investimento (e a chave "elegibilidade" recebe o valor 0).

## Atualização dos Objetos de Cliente
O código verifica a elegibilidade de cada cliente e adiciona a chave "elegibilidade" aos objetos de cliente com o valor correspondente (0 ou 1).

## Mensagens de Marketing Personalizadas
Além de determinar a elegibilidade, o código gera mensagens de marketing personalizadas para cada cliente com base em sua elegibilidade. Se o cliente for elegível para empréstimo, uma mensagem indicando a oferta de empréstimo é gerada. Se o cliente for elegível para investimento, uma mensagem sobre a oportunidade de investimento é gerada.

## Impressão de Resultados
Finalmente, o código imprime os objetos de cliente atualizados com a chave "elegibilidade" e as mensagens de marketing correspondentes. Isso permite que você veja claramente a elegibilidade de cada cliente e a mensagem que receberiam.

Esse programa é um exemplo simples de como podemos usar Python para automatizar tarefas de negócios, como determinar a elegibilidade de clientes e enviar mensagens personalizadas com base nessa elegibilidade. Podemos personalizar ainda mais esse código de acordo com as necessidades do projeto.

***
***

Cliente ID 6489 - Nome: Maria De Lourdes, Elegibilidade: 0
***
Cliente ID 2755 - Nome: Cinésio Oliveira, Elegibilidade: 1
***
Cliente ID 7734 - Nome: Domênico Vespúcio, Elegibilidade: 0
***
Cliente ID 8631 - Nome: Cátia Prado, Elegibilidade: 1
***
Cliente ID 2383 - Nome: Janete Pereira, Elegibilidade: 0

***
***

Cliente ID 6489 - Nome: Maria De Lourdes, Elegibilidade: 0, Mensagem:

Olá, Maria De Lourdes! Temos uma excelente oportunidade de investimento para você. Entre em contato para saber mais e fazer seu dinheiro render.


Cliente ID 2755 - Nome: Cinésio Oliveira, Elegibilidade: 1, Mensagem: 

Prezado(a) Cinésio Oliveira, você é elegível para um empréstimo especial. Entre em contato conosco para obter mais detalhes.


Cliente ID 7734 - Nome: Domênico Vespúcio, Elegibilidade: 0, Mensagem:

Olá, Domênico Vespúcio! Temos uma excelente oportunidade de investimento para você. Entre em contato para saber mais e fazer seu dinheiro render.


Cliente ID 8631 - Nome: Cátia Prado, Elegibilidade: 1, Mensagem: 

Prezado(a) Cátia Prado, você é elegível para um empréstimo especial. Entre em contato conosco para obter mais detalhes.


Cliente ID 2383 - Nome: Janete Pereira, Elegibilidade: 0, Mensagem: 

Olá, Janete Pereira! Temos uma excelente oportunidade de investimento para você. Entre em contato para saber mais e fazer seu dinheiro render.
