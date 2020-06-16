valor = int(input('Valor a ser sacado: R$'))
total = valor
cedula = 50
totCed = 0
while True:
    if total >= cedula:
        total -= cedula
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCed = 0
        if total == 0:
            break
print('FIM!')