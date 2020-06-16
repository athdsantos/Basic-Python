cont_total_compra = produto_barato = 0.0
cont_mais_1k = cont = 0
cont_produto_barato = escolha = novoProduto = ''
while escolha in 'Ss':

    produto = input('Digite o produto: ')
    preco_produto = float(input('Preço do produto: R$'))
    cont += 1
    cont_total_compra += preco_produto

    if preco_produto > 1000.00:
        cont_mais_1k += 1

    if cont == 1 or preco_produto < produto_barato:
       produto_barato = preco_produto
       produto_barato = produto
    escolha = ''
    '''if preco_produto < produto_barato:
        produto_barato = preco_produto
        novoProduto = produto'''

    escolha = input('\nDeseja continuar? [S/N] ').upper().strip()[0]
    if escolha not in 'Nn' and escolha not in 'Ss':
        while escolha not in 'Nn' and escolha not in 'Ss':
            print('Favor inserir um valor correto [S/N]!')
            escolha = input('\nDeseja continuar? [S/N] ')

    if escolha in 'Nn':
        break
print(f'\nFIMM\nTotal: R${cont_total_compra:.2f}\nProdutos mais que R$1000: {cont_mais_1k}\nProduto mais barato: {novoProduto}')
