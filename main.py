from department import Department
from university import University
from department import Department
from teacher import Teacher
from discipline import Disciplines
import random

# criando uma instância para as classes
uni = University("Escola Superior de Tecnologia", "Amazonas")
dep = Department("\nProfessores:")
prof = Teacher()

# Criando uma instância da classe Disciplines
disciplinas = Disciplines()


# exibindo as informações da universidade
print(f"Universidade: {uni.name}, Localização: {uni.location}")

# adicionando departamentos
uni.add_department(type("Department", (), {"name": "Engenharia Eletrônica"}))
uni.add_department(type("Department", (), {"name": "Engenharia de Computação"}))
uni.add_department(type("Department", (), {"name": "Engenharia de Produção"}))
uni.add_department(type("Department", (), {"name": "Sistemas de Informação"}))

#adicionando professores
prof.adicionar_professor("Jucimar Maia")
prof.adicionar_professor("Elloa Barreto")
prof.adicionar_professor("Luis Cuevas")
prof.adicionar_professor("Polianny Almeida")
prof.adicionar_professor("Ricardo Barboza")



print("Departamentos:")
for dept in uni.list_departments():
    print(f"- {dept}")

print(dep.name)
dep.add_teacher(type("Teacher", (), {"name": "Jucimar Maia"}))
dep.add_teacher(type("Teacher", (), {"name": "Elloa Baareto"}))
dep.add_teacher(type("Teacher", (), {"name": "Luís Cuevas"}))
dep.add_teacher(type("Teacher", (), {"name": "Polliany Almeida"}))
dep.add_teacher(type("Teacher", (), {"name": "Ricardo Barboza"}))

for dept in dep.list_teachers():
    print(f"- {dept}")


# Função para atribuir disciplinas
def atribuir_disciplinas_para_professores():
    for professor in prof.lista_professores:
        # Seleciona aleatoriamente 5 disciplinas
        import random
        professor_disciplinas = random.sample(disciplinas.disciplinas, 5)
        print(f"\nProfessor {professor} foi atribuído a seguinte lista de disciplinas:")
        for disciplina in professor_disciplinas:
            print(f"- {disciplina}")

# Atribuindo disciplinas para os professores
atribuir_disciplinas_para_professores()



