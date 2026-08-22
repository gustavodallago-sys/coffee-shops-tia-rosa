# Listas globais responsáveis por armazenar os dicionários do sistema.

produtos = []
clientes = []
pedidos = []

# Funções relativas aos produtos: Menu, Cadastro e Listagem


def menu_produtos():
    while True:
        print()

        print('=-' * 20)
        print('=-=-=-=-=Menu de produtos=-=-=-=-=')
        print('=-' * 20)

        print('1 - Cadastrar Produto')
        print('2 - Listar Produtos')
        print('0 - Voltar ao Menu Pincipal')
        print()

        # Testa se a opção digitada pode ser convertida num inteiro, caso contrário, será exibida uma mensagem de erro.
        try:
            opc_prod = int(input('Digite uma opção: '))

        except ValueError:
            print('OPÇÃO INVÁLIDA, DIGITE APENAS NÚMEROS')
            continue


        if opc_prod == 1:
            print()
            cadastrar_produtos()

        elif opc_prod == 2:
            print()
            listar_produtos()

        elif opc_prod == 0:
            print('Voltando ao Menu Principal')
            break
        else:
            print('OPÇÃO INVÁLIDA. INSIRA UMA OPÇÃO ACIMA.')

def cadastrar_produtos():
    print('=-' * 20)
    print('=-=-=-=-=CADASTRO DE PRODUTO=-=-=-=-=')
    print('=-' * 20)


    while True:
        nome_prod = input('Digite o nome do produto: ').strip().title()
        if nome_prod == '':
            print('O CAMPO DEVE CONTER UM NOME.')
        else:
            break

    while True:

        # Teste de valor permitido para um produto, se for menor ou igual a zero, não será aceito.
        try:
            preco_produto = float(input('Digite o preço do produto: R$ '))
            if preco_produto <= 0:
                print('O PREÇO DEVE SER MAIOR QUE ZERO.')

            # Se o preço for permitido (sendo maior que 0), o sistema aceita.
            else:
                break

        except ValueError:
            print('O PREÇO DEVE CONTER APENAS NÚMEROS!')

    while True:
        try:
            qtd_estoque = int(input('Digite a quantidade de estoque: '))
            if qtd_estoque < 0:
                print('O NÚMERO NÃO PODE SER MENOR QUE ZERO.')

            else:
                break
        except ValueError:
            print('O VALOR DIGITADO PRECISA SER UM NÚMERO INTEIRO.')

    while True:

        desc_produto = input('Digite a descrição do produto: ').strip()
        if desc_produto == '':
            print('INSIRA UMA DESCRIÇÃO SIMPLES DO PRODUTO.')
        else:
            break

    # Aqui, gera o próximo código somando 1 à quantidade de produtos já cadastrados na lista.
    cod_produto = len(produtos) + 1


    # Esse dicionário será um elemento da lista global "produtos"
    produto = {
        'codigo_produto': cod_produto,
        'nome_produto': nome_prod,
        'preco_produto': preco_produto,
        'desc_produto': desc_produto,
        'qtd_estoque': qtd_estoque
    }

    produtos.append(produto)
    print('PRODUTO ADICIONADO COM SUCESSO!')
    print()

def listar_produtos():
    print('=-' * 20)
    print('=-=-=-=-=LISTA DE PRODUTOS=-=-=-=-=')
    print('=-' * 20)

    qtd_prod_ver = len(produtos)

    if qtd_prod_ver == 0:
        print('Nenhum produto foi cadastrado')

    else:

        # Laço que mostra todos os produtos listados, elemento por elemento da lista global "produtos"
        for produto in produtos:
            print('-'*20)
            print(f'Código: {produto["codigo_produto"]}')
            print(f'Produto: {produto["nome_produto"]}')
            print(f'Descrição: {produto["desc_produto"]}')
            print(f'Preço: R$ {produto["preco_produto"]:.2f}')
            print(f'Quantidade: {produto["qtd_estoque"]} unidade(s)')
            print('-' * 20)
            print()


# Funções relativas aos clientes: Menu, Cadastro e Listagem


def menu_clientes():
    while True:
        print()
        print('=-' * 20)
        print('=-=-=-=-=Menu de Clientes=-=-=-=-=')
        print('=-' * 20)

        print('1 - Cadastrar Cliente')
        print('2 - Listar Clientes')
        print('0 - Voltar ao Menu Pincipal')
        print()

        try:
            opc = int(input('Digite uma opção: '))

        except ValueError:
            print('OPÇÃO INVÁLIDA, DIGITE APENAS NÚMEROS')
            continue

        if opc == 1:
            novo_cliente()

        elif opc == 2:
            listar_clientes()

        elif opc == 0:
            break

        else:
            print('OPÇÃO INVÁLIDA. INSIRA UMA OPÇÃO ACIMA.')

def novo_cliente():
    print('=-' * 20)
    print('=-=-=-=-=NOVO CLIENTE=-=-=-=-=')
    print('=-' * 20)
    print()
    while True:
        nome_cliente = input('Digite o nome do cliente: ').strip().title()
        if nome_cliente == '':
                print('INSIRA UM NOME.')
        else:
            break

    while True:
        numero_telefone = input('Digite o telefone do cliente: ').strip()

        # Verificação de validade do número de telefone digitado.
        if numero_telefone.isdigit():

            # Validação se o número de telefone tem entre 10 e 11 dígitos.
            qtd_digitos = len(numero_telefone)
            if 10 <= qtd_digitos <= 11:
                break
            else:
                print('NÚMERO INVÁLIDO, PRECISA CONTER ENTRE 10 E 11 NÚMEROS')
                continue

        else:
            print('DIGITE APENAS NÚMEROS!')
            continue

    cod_cliente = len(clientes) + 1

    # Todo cliente novo terá pontuação 0.
    pontos_iniciais = 0

    cliente = {
        'codigo_cliente': cod_cliente,
        'nome_cliente': nome_cliente,
        'numero_telefone': numero_telefone,
        'pontos': pontos_iniciais
    }

    # Adição do dicionário criado na lista global "clientes"
    clientes.append(cliente)

    print(f'O cliente {cliente['nome_cliente']} foi cadastrado com sucesso! Códido: {cliente["codigo_cliente"]}.')

def listar_clientes():
    print('=-' * 20)
    print('=-=-=-=-=LISTA DE CLIENTES=-=-=-=-=')
    print('=-' * 20)

    qtd_clientes = len(clientes)
    if qtd_clientes == 0:
        print('Nenhum cliente foi cadastrado')
    else:
        for cliente in clientes:
            print('-' * 20)
            print(f'Código: {cliente["codigo_cliente"]}')
            print(f'Nome: {cliente["nome_cliente"]}')
            print(f'Telefone: {cliente["numero_telefone"]}')
            print(f'Pontos: {cliente["pontos"]} ponto(s)')
            print('-' * 20)
            print()

# Funções auxiliares de busca: clientes e produtos
# Essas retornam os dicionários que vão utilizadas nas funções seguintes.

def busca_cliente_cod(cod_cliente):
    for cliente in clientes:
        if cliente['codigo_cliente'] == cod_cliente:
            return cliente

    return None

def busca_produto_cod(cod_produto):
    for produto in produtos:
        if produto['codigo_produto'] == cod_produto:
            return produto

    return None


# Registro de pedidos

def registrar_pedido():

    # Veerificação da existência de Clientes e Produtos nas listas globais
    if clientes == [] :
        print('NENHUM CLIENTE CADASTRADO.')
        return

    if produtos == []:
        print('NENHUM PRODUTO CADASTRADO.')
        return

    listar_clientes()

    # Aqui a seleção de Clientes acontece, com teste de validação de tipo de dado inserido pelo usuário.
    while True:
        try:
            cod_cliente = int(input('Digite o codigo do cliente: '))
        except ValueError:
            print('INSIRA APENAS NÚMEROS.')
            continue

        cliente_encontrado = busca_cliente_cod(cod_cliente)

        if cliente_encontrado == None:
            print('Cliente não encontrado.')
            continue
        else:
            break

    listar_produtos()

    # Aqui a seleção de Produtos acontece, com teste de validação de tipo de dado inserido pelo usuário.
    while True:

        try:
            cod_produto = int(input('Digite o codigo do produto: '))
        except ValueError:
            print('DIGITE APENAS NÚMEROS.')
            continue

        produto_encontrado = busca_produto_cod(cod_produto)

        if produto_encontrado == None:
            print('Produto não encontrado.')
            continue

        elif produto_encontrado['qtd_estoque'] == 0:
            print('Produto esgotado. Selecione outro.')
            continue

        else:
            break

    # Aqui a seleção da quantidade de produtos que será pedida.
    while True:
        try:
            quantidade = int(input('Digite a quantidade de produtos: '))
        except ValueError:
            print('DIGITE APENAS NÚMEROS.')
            continue

        # Verificação da disponibilidade de produtos em relação à quantidade pedida.
        if quantidade <= 0:
            print('A quantidade deve ser maior que zero.')
            continue

        elif quantidade > produto_encontrado['qtd_estoque']:
            print('Quantidade não disponível em estoque.')
            continue

        else:
            break

    # Essa linha evita que 2 ou mais pedidos tenham o mesmo código, adicionando 1 ao seu número.
    cod_pedido = len(pedidos) + 1

    preco = produto_encontrado['preco_produto']

    # Cálculo do total do pedido pela quantidade de produtos solicitada.
    total_pedido = preco * quantidade


    # Regra de fidelização: a cada R$ 10 em compras, o cliente ganha 1 ponto.
    pontos_ganhos = int(total_pedido // 10)

    # Essa linha atualiza, no dicionário do cliente que faz o pedido, a quantidade de pontos que ele tem.
    cliente_encontrado['pontos'] += pontos_ganhos

    # Atualização do estoque de produtos em relação à quantidade que foi pedida.
    produto_encontrado['qtd_estoque'] -= quantidade


    # Criação do dicionário do pedido
    pedido = {
        'codigo_pedido': cod_pedido,
        'cod_cliente': cliente_encontrado['codigo_cliente'],
        'nome_cliente': cliente_encontrado['nome_cliente'],
        'cod_produto': produto_encontrado['codigo_produto'],
        'nome_produto': produto_encontrado['nome_produto'],
        'quantidade': quantidade,
        'preco_unitario': preco,
        'total': total_pedido,
        'pontos': pontos_ganhos,
}


    # Ele é adicionado à lista global aqui.
    pedidos.append(pedido)

    print(f'PEDIDO REGISTRADO COM SUCESSO!')
    print('-'*20)
    print(f'Código do pedido: {pedido['codigo_pedido']}')
    print(f'Cliente: {pedido['nome_cliente']}')
    print(f'Produto: {pedido['nome_produto']}')
    print(f'Quantidade: {pedido['quantidade']}')
    print(f'Total: R$ {pedido['total']:.2f}')
    print(f'Pontos Ganhos: {pedido['pontos']}')
    print('-'*20)

# Relatório de vendas

def relatorio_vendas():

    print('-'*20)
    print('=-=-=-=-=RELATÓRIO DE VENDAS=-=-=-=-=')
    print('-' * 20)

    # Essa condição verifica se a lista "pedidos" possui algum elemento (pedido)
    if pedidos == []:
        print('Nenhuma venda foi registrada.')
        return

    # Inicializa o acumulador utilizado para somar o valor de todos os pedidos.
    total_vendido = 0

    for pedido in pedidos:
        print(f'Pedido: {pedido['codigo_pedido']}')
        print(f'CLiente: {pedido["nome_cliente"]}')
        print(f'Produto: {pedido["nome_produto"]}')
        print(f'Quantidade: {pedido["quantidade"]}')
        print(f'Total: R$ {pedido["total"]:.2f}')
        print(f'Pontos ganhos: {pedido["pontos"]}')
        print('-'*20)

        total_vendido += pedido["total"]

        print()

    # Resumo geral das vendas.
    print(f'Quantidade de pedidos: {len(pedidos)}')
    print(f'Total vendido: R$ {total_vendido:.2f}')






# Programa Principal


print('=-'*20)
print('=-=-=-=-=COFFEE SHOPS TIA ROSA=-=-=-=-=')
print('=-'*20)





# Laço do menu principal.


while True:
    print()
    print('MENU PRINCIPAL')
    print('1 - Gerenciar Produtos')
    print('2 - Gerenciar Clientes')
    print('3 - Registrar Pedidos')
    print('4 - Visualizar Relatório')
    print('0 - Sair do Sistema')
    print()


    # Verificação de validade do que foi digitado pelo usuário.
    try:
        opc = int(input('Escolha uma opção: '))

    except ValueError:
        print('OPÇÃO INVÁLIDA, DIGITE APENAS NÚMEROS')
        print()
        continue

    if opc == 1:
        menu_produtos()
        print()

    elif opc == 2:
        menu_clientes()
        print()

    elif opc == 3:
        registrar_pedido()
        print()

    elif opc == 4:
        relatorio_vendas()
        print()

    elif opc == 0:
        print('Encerrando o Sistema')
        break

    else:
        print('OPÇÃO INVÁLIDA. INSIRA UMA OPÇÃO ACIMA.')
        print()
