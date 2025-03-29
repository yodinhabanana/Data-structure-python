

import time

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self,item):
        self.itens.append(item)
    
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        
        return "A pilha está vazia"
    
    def topo(self):
        if not self.esta_vazia():
            print("Topo da pilha: ", self.itens[-1])
        else:
            print("A pilha está vazia.")
    
    def esta_vazia(self):
        if len(self.itens) == 0:
            return True
        else:
            return False
    
    def tamanho(self):
        return len(self.itens)
    
    def remocao(self, referencia):
        if referencia in self.itens:
            self.itens.remove(referencia)
            print(f"Item '{referencia}' removido.")
        else:
            print("Item não encontrado na pilha.")

pilha = Pilha()

while True:
    print("\nO que deseja fazer?")
    print("1. Adicionar item na pilha")
    print("2. Espiar o topo.")
    print("3. Tirar o topo.")
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
            pilha.empilhar(item)
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == 2:
        pilha.topo()

    elif opcao == 3:
        print("Desempilhando: ", pilha.desempilhar())

    elif opcao == 4:
        print("Tamanho: ", pilha.tamanho())

    elif opcao == 5:
        try:
            ref = int(input("Digite o número inteiro que deseja remover: "))
            pilha.remocao(ref)
        except ValueError:
            print("Opção inválida, digite uma opção válida")

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
