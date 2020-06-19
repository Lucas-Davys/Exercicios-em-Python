

peso_peixe = float(input('Informe o peso do peixe: '))

peso_excesso = peso_peixe - 50

if peso_excesso > 0:
   multa = peso_excesso*4.00
   print('\nO peixe está acima do {} quilos acima do limite. Você deverá pagar uma multa de R$ {} '.format(peso_excesso,multa))
else:
   print('O peso do peixe está dentro do limite')