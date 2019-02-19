lista = []
execute = True
max = 0

while execute:
    x = int(input('Digite o valor de x, ou 0 para terminar: '))
    if(x != 0):
        lista.append(x)
    elif(x==0):
        execute = False
print(lista)

for i in range(len(lista)):
    if(lista[i] > max):
        max = lista[i]
print(max)


min = max
for a in range(len(lista)):
    if(lista[a] < min):
        min = lista[a]
print(min)