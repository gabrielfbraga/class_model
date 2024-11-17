class Disciplines:
    def __init__(self):
        self.disciplinas = [
            "Matemática Discreta", "Algoritmos e Estruturas de Dados", "Redes de Computadores",
            "Cálculo 1", "Cálculo 2", "Cálculo 3", "Programação Orientada a Objetos", "Banco de Dados",
            "Engenharia de Software", "Sistemas Operacionais", "Teoria dos Grafos", "Inteligência Artificial",
            "Redes Neurais", "Compiladores", "Arquitetura de Computadores", "Linguagens Formais e Autômatos",
            "Teoria da Computação", "Processamento de Imagens", "Desenvolvimento Web", "Segurança da Informação",
            "Sistemas Distribuídos", "Interfaces de Usuário", "Prática em Programação", "Ética em TI", "Gestão de Projetos de TI"
        ]
    
    def __str__(self):
        # Retorna a lista de disciplinas como uma string formatada
        return "\n".join(self.disciplinas)
