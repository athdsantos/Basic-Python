tuplaPalavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
                 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print('-' * 40)
print(f'{"VOGAIS NAS PALAVRAS":^40}')
print('-' * 40)
for p in tuplaPalavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for v in p:
        if v.lower() in 'AEIOUaeiou':
            print(v, end=' ')