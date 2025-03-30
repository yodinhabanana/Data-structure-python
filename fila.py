

import time

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self,item):
        self.itens.append(item)
        print(f"{item} entrou na fila.")

    def desenfileirar(self):
        if not self.esta_vazia():
            removido = self.itens.pop(0)
            print(f"{removido} entrou na fila.")
            return removido
        else:
            print("A fila está vazia! Nada para remover.")
            return None
        
    def esta_vazia(self):
        return len(self.itens) == 0

    def mostrar_primeiro(self):
        print("Primeiro elemento: ", self.itens[0])
    
    def mostrar_fila(self):
        print("Fila atual:", self.itens)

    def tamanho(self):
        return len(self.itens1)

fila = Fila()

while True:
    print("\nO que deseja fazer?")
    print("1. Adicionar item na fila")
    print("2. Ver primeiro elemento.")
    print("3. Tirar o primeiro.")
    print("4. Mostrar o tamanho.")
    print("5. Remoção de item especifico.")
    print("6. Sair.")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        
    if opcao == 1:
        try:
            item = int(input("Digite um número: ")) 
            fila.enfileirar(item)
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == 2:
        fila.mostrar_primeiro()

    elif opcao == 3:
        print("Desenfileirando: ", fila.desenfileirar())

    elif opcao == 4:
        print("Tamanho: ", fila.tamanho())

    elif opcao == 6:

        print("Saindo", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)  
        print(".", end="")
        time.sleep(1)  
        print(".")
        break

    else:
        print("Opção inválida, tente novamente.")
