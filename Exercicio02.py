#2. (6.0) O jogo "Whack-a-Mole" é um jogo divertido onde toupeiras aparecem aleatoriamente em diferentes
#buracos, e o objetivo do jogador é acertar as toupeiras que surgem. Neste exercício, vamos simular uma versão
#simplificada do surgimento das toupeiras do jogo utilizando uma matriz 4x4. A cada ciclo, quatro toupeiras
#aparecerão em posições aleatórias dentro da matriz, representadas pelo símbolo 'T', enquanto os buracos restantes
#estarão vazios, representados pelo símbolo '-'. Sua tarefa é gerar e exibir três gerações diferentes dessas matrizes.
import random

#função geradora
def gerarToupeiras(ng):
    geracao=0
    while ng!=0:
        geracao=geracao+1
        print('Geração:',geracao)
        #gerar matrix 4x4 com '-'
        M=[]
        nLinhas=4
        nColunas=4
        n=0
        for i in range(nLinhas):
            novaLinha=[]
            for j in range(nColunas):
                novoElemento='-'
                novaLinha.append(novoElemento)
            M.append(novaLinha)
        #colocador de toupeira em M com limite de numero de 4 touperas
        while n!=4: #n é o limitador de touperas
            i=random.randint(0,3)
            j=random.randint(0,3)
            if M[i][j]=='T':
                pass
            elif M[i][j]=='-': #verifica se o espaço esta vazio
                M[i][j]='T'
                n=n+1
        
        #leitor
        for i in range(len(M)):
            for j in range(len(M[0])):
                print(M[i][j], end="\t")
            print()
        print()
        #cont de gerações 
        ng=ng-1

###MAIN### 
ng=3 #numero de gerações pode ser alterado para realizar mais gerações de toupeiras 
M=gerarToupeiras(ng)




