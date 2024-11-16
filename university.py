class University:

    def __init__(self, name, location):
        self.name = name  
        self.location = location  
        self.departments = [] 

    def add_department(self, department):
        """Adiciona um departamento à universidade."""
        self.departments.append(department)

    def list_departments(self):
        """Retorna uma lista com os nomes dos departamentos."""
        return [department.name for department in self.departments]