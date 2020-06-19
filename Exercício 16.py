
area = float(input('\nInforme, em metros quadrados, a área a ser pintada: '))

quantidade_tinta = area/6
quantidade_latas = quantidade_tinta/18
quantidade_galoes = quantidade_tinta/3.6
preco_total_latas = 80 * quantidade_latas
preco_total_galoes = 25 * quantidade_galoes

print('\nVocê vai precisar de {} latas e o custo total vai ser de R$ {}'.format(quantidade_latas,preco_total_latas))
