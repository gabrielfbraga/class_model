class Department:
    def __init__(self):
        self.departamentos = [
            "Engenharia Eletrônica",
            "Engenharia de Computação",
            "Engenharia de Produção",
            "Sistemas de Informação",
            "Licenciatura em computação"
        ]

    def __str__(self):
        print("Departamentos:")
        return "\n".join(self.departamentos)