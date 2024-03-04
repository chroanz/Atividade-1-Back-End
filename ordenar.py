lista = [12, 2, 5, 1, 3, 7, 7968]
tamanho = len(lista)

for i in range(tamanho):
  for j in range(0, tamanho - i - 1):
    if lista[j] > lista[j + 1]:
      lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
