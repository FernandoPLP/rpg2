class Mochila:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.itens = []

    def adicionar_item(self, item):
        if len(self.itens) < self.capacidade_maxima:
            self.itens.append(item)
            print(f"{item} foi adicionado à mochila.")
        else:
            print("A mochila está cheia!")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} foi removido da mochila.")
        else:
            print(f"{item} não está na mochila.")

    def listar_itens(self):
        if self.itens:
            print("Itens na mochila:")
            for item in self.itens:
                print(item)
        else:
            print("A mochila está vazia.")

# Exemplo de uso
mochila_do_jogador = Mochila(5)  # Mochila com capacidade máxima de 5 itens

mochila_do_jogador.adicionar_item("Espada")
mochila_do_jogador.adicionar_item("Poção de Cura")
mochila_do_jogador.adicionar_item("Escudo")
mochila_do_jogador.listar_itens()

mochila_do_jogador.remover_item("Poção de Cura")
mochila_do_jogador.listar_itens()
