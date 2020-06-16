resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = float(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Quer continuar? ').strip().upper()[0]
media = soma / quant
print('Quantidade: {}\nSoma: {}\nMédia: {:.1f}\nMaior: {}\nMenor: {}'.format(quant, soma, media, maior, menor))
