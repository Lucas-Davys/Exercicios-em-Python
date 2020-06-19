
area = float(input('\nInforme, em metros quadrados, a área a ser pintada: '))

quantidade_tinta = area/3
quantidade_latas = quantidade_tinta/18
preco_total = 80 * quantidade_latas

print('\nVocê vai precisar de {} latas e o custo total vai ser de R$ {}'.format(quantidade_latas,preco_total))
