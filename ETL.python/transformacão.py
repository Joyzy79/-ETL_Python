# Dados dos clientes
clientes = [
    {
        'id': 6489,
        'name': 'Maria De Lourdes',
        'account': {'id': 6746, 'number': '15843-4', 'agency': '1013', 'balance': 0, 'limit': 1.870},
        'card': {'id': 3349, 'number': '**** **** **** 9909', 'limit': 1600}
    },
    { 
        'id': 2755,
        'name': 'Cinésio Oliveira',
        'account': {'id': 9667, 'number': '84104-3', 'agency': '1013', 'balance': 0, 'limit': 500},
        'card': {'id': 4426, 'number': '**** **** **** 4306', 'limit': 1000}
    },
    {
        'id': 7734,
        'name': 'Domênico Vespúcio',
        'account': {'id': 711, 'number': '80804-3', 'agency': '1013', 'balance': 0, 'limit': 6.786},
        'card': {'id': 9294, 'number': '**** **** **** 7960', 'limit': 2200}
    },
    {
        'id': 8631,
        'name': 'Cátia Prado',
        'account': {'id': 1028, 'number': '54359-5', 'agency': '1013', 'balance': 0, 'limit': 287},
        'card': {'id': 8426, 'number': '**** **** **** 2663', 'limit': 1000}
    },
    {
        'id': 2383,
        'name': 'Janete Pereira',
        'account': {'id': 8551, 'number': '93764-4', 'agency': '1013', 'balance': 0, 'limit': 2200},
        'card': {'id': 508, 'number': '**** **** **** 2356', 'limit': 1600}
    }
]

# Função para determinar a elegibilidade de empréstimo ou investimento
def determinar_elegibilidade(cliente):
    if cliente['account']['limit'] < cliente['card']['limit']:
        cliente['elegibilidade'] = 1  
        return f"Prezado(a) {cliente['name']}, você é elegível para um empréstimo especial. Entre em contato conosco para obter mais detalhes."
    else:
        cliente['elegibilidade'] = 0 
        return f"Olá, {cliente['name']}! Temos uma excelente oportunidade de investimento para você. Entre em contato para saber mais e fazer seu dinheiro render."

# Verificar a elegibilidade de cada cliente e adicionar a chave "elegibilidade" aos objetos
for cliente in clientes:
    determinar_elegibilidade(cliente)

# Imprimir os objetos de cliente atualizados com a chave "elegibilidade"
for cliente in clientes:
    print(f"Cliente ID {cliente['id']} - Nome: {cliente['name']}, Elegibilidade: {cliente['elegibilidade']}")

# Imprimir os objetos de cliente atualizados com a chave "elegibilidade" e o texto de elegibilidade
for cliente in clientes:
    print(f"Cliente ID {cliente['id']} - Nome: {cliente['name']}, Elegibilidade: {cliente['elegibilidade']}, Mensagem: {determinar_elegibilidade(cliente)}")