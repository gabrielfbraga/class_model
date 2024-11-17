from department import Department
from university import University
from department import Department
from teacher import Teacher
from discipline import Disciplines

# criando uma instância para as classes
uni = University("Escola Superior de Tecnologia", "Amazonas")
dep = Department("Departamentos:")
prof = Teacher()

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
dep.add_teacher(type("Teacher", (), {"name": "Jucimar"}))
dep.add_teacher(type("Teacher", (), {"name": "Elloa"}))
dep.add_teacher(type("Teacher", (), {"name": "Ponciano"}))
dep.add_teacher(type("Teacher", (), {"name": "Anderson"}))
dep.add_teacher(type("Teacher", (), {"name": "Ponciano"}))

for dept in dep.list_teachers():
    print(f"- {dept}")


