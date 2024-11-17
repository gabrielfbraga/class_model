class Teacher:
    def __init__(self):
        self.lista_professores = []  # Lista para armazenar os nomes

    def adicionar_professor(self, nome):
        """Adiciona o nome de um professor à lista."""
        if nome not in self.lista_professores:
            self.lista_professores.append(nome)
            print(f"Professor {nome} adicionado com sucesso!")
        else:
            print(f"Professor {nome} já está na lista.")

    def listar_professores(self):
        """Retorna a lista de professores."""
        if not self.lista_professores:
            print("Nenhum professor cadastrado ainda.")
        else:
            print("Lista de professores:")
            for i, professor in enumerate(self.lista_professores, 1):
                print(f"{i}. {professor}")

    def remover_professor(self, nome):
        """Remove um professor da lista, se existir."""
        if nome in self.lista_professores:
            self.lista_professores.remove(nome)
            print(f"Professor {nome} removido com sucesso!")
        else:
            print(f"Professor {nome} não encontrado na lista.")
