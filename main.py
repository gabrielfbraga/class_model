from university import University
from department import Department
from teacher import Teacher
from discipline import Disciplines
import random

# criando uma instância para as classes
uni = University("Escola Superior de Tecnologia", "Amazonas")
departamento = Department()
prof = Teacher()
disciplinas = Disciplines()

# exibindo as informações da universidade
print(f"Universidade: {uni.name}, Localização: {uni.location}")
print("\n")
print(f"{disciplinas}")
print("\n")
print(f"{departamento}")
print("\n")
print(f"{prof}")

# Função para atribuir disciplinas
def atribuir_disciplinas_para_professores():
    for professor in prof.professores:
        # Seleciona aleatoriamente 5 disciplinas
        import random
        professor_disciplinas = random.sample(disciplinas.disciplinas, 5)
        print(f"\nProfessor {professor} foi atribuído a seguinte lista de disciplinas:")
        for disciplina in professor_disciplinas:
            print(f"- {disciplina}")

# Atribuindo disciplinas para os professores
atribuir_disciplinas_para_professores()

def atribuir_profs_depart():

    for professor in prof.professores:  # Corrigido para acessar a lista de professores
        # Escolhe um departamento aleatório
        professor_dep = random.choice(departamento.departamentos)
        print(f"\nProfessor {professor} foi atribuído ao seguinte departamento:")
        print(f"- {professor_dep}")  # Assumindo que os departamentos têm um atributo 'name'

# Atribuindo disciplinas para os professores
atribuir_profs_depart()
