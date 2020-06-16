def notas(*n, sit=False):
    """
    Função que analisa a situação do aluno
    :param n: nota dos alunos (uma ou várias notas)
    :param sit: Situação do aluno de acordo com a média
    :return: retorna o dicionário com as informações
    """
    info_notas = {'quantidade_notas': len(n), 'maior_nota': max(n), 'menor_nota': min(n), 'media': sum(n) / len(n)}
    if sit:
        if info_notas['media'] >= 7:
            info_notas['situacao'] = 'ÓTIMO'
        elif info_notas['media'] <= 5:
            info_notas['situacao'] = 'RUIM'
        else:
            info_notas['situacao'] = 'RAZOÁVEL'
    return info_notas


print(notas(1.0, 2, 10, sit=False))
