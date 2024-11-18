from university import University
from department import Department
from teacher import Teacher
from discipline import Disciplines
import random

# Criando instâncias para as classes (opcional para University e Department)
try:
    uni = University("Escola Superior de Tecnologia", "Amazonas")
except TypeError:
    uni = None

try:
    departamento = Department()
except TypeError:
    departamento = None

prof = Teacher()
disciplinas = Disciplines()

# Exibindo as informações da universidade, se ela for válida
if uni:
    print(f"Universidade: {uni.name}, Localização: {uni.location}")
else:
    print("Nenhuma universidade foi informada.")
print("\n")

# Exibindo as disciplinas
print(f"{disciplinas}")
print("\n")

# Exibindo os departamentos (apenas se a universidade existir)
if uni and departamento:
    print(f"{departamento}")
else:
    print("Departamentos não serão exibidos porque a universidade não foi informada.")
print("\n")

# Exibindo os professores
print(f"{prof}")

# Função para atribuir disciplinas
def atribuir_disciplinas_para_professores():
    for professor in prof.professores:
        # Seleciona aleatoriamente 5 disciplinas
        professor_disciplinas = random.sample(disciplinas.disciplinas, 5)
        print(f"\nProfessor {professor} foi atribuído a seguinte lista de disciplinas:")
        for disciplina in professor_disciplinas:
            print(f"- {disciplina}")

# Função para atribuir professores a departamentos
def atribuir_profs_depart():
    # Apenas executa se a universidade e os departamentos forem válidos
    if not (uni and departamento):
        print("Universidade ou departamentos não informados. Atribuição de professores a departamentos será ignorada.")
        return

    for professor in prof.professores:
        # Escolhe um departamento aleatório
        professor_dep = random.choice(departamento.departamentos)
        print(f"\nProfessor {professor} foi atribuído ao seguinte departamento:")
        print(f"- {professor_dep}")

# Atribuindo disciplinas para os professores
atribuir_disciplinas_para_professores()

# Atribuindo professores a departamentos (apenas se a universidade e os departamentos existirem)
atribuir_profs_depart()