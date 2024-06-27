#1. (4.0 pts) Implementando o próprio “shuffle” em arrays: faça um algoritmo que receba um array e embaralhe os
#seus elementos da seguinte maneira: por n vezes (n é o tamanho do array) ele deve sortear dois índices, i e j, e trocá-
#los de lugar.
import random

#função
def embaralhar(V):
    n=len(V)
    print('o vetor foi embaralhado',n,'vezes')
    for x in range(n): #repetidor
        #seletor de indices
        i=random.randint(0,n-1)
        j=i 
        while i==j: #garantindo que i e j são diferentes(opcional)
            j=random.randint(0,n-1)

        #dois elementos selecionados por i e j
        E1=V[i]
        E2=V[j]
        #trocas
        V[j]=E1
        V[i]=E2
        #print(V) #retirar comentario para ver uma mudança de cada vez
        x+=x #contador de vezes

###MAIN###

#vetor inicial modificavél|(numeros e letras)
V=['a','b','c','d','e','f']
print('o vetor inicial é',V)
#chamado função
embaralhar(V)
#resultado embaralhado
print('o vetor embaralhado é',V)