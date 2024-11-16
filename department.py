class Department:

    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        """Adiciona um professor ao departamento."""
        self.teachers.append(teacher)

    def list_teachers(self):
        """Retorna uma lista com os nomes dos professores."""
        return [teacher.name for teacher in self.teachers]