class Teacher:
    def __init__(self):
        self.professores = [
            "Jucimar Maia",
            "Elloa Barreto",
            "Luis Cuevas",
            "Polianny Almeida",
            "Ricardo Barboza"
        ]  # Lista para armazenar os nomes
    def __str__(self):
        print("Professores:")
        return "\n".join(self.professores)
