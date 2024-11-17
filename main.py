from department import Department
from university import University
from department import Department
from teacher import Teacher
from discipline import Disciplines

# criando uma instância da classe University
uni = University("Escola Superior de Tecnologia", "Amazonas")

dep = Department("Professores:")

# exibindo as informações da universidade
print(f"Universidade: {uni.name}, Localização: {uni.location}")

# adicionando departamentos
uni.add_department(type("Department", (), {"name": "Engenharia Civil"}))
uni.add_department(type("Department", (), {"name": "Engenharia Eletrônica"}))  
uni.add_department(type("Department", (), {"name": "Engenharia Elétrica"}))  
uni.add_department(type("Department", (), {"name": "Engenharia Mecatrônica"}))  
uni.add_department(type("Department", (), {"name": "Engenharia Mecânica"}))  
uni.add_department(type("Department", (), {"name": "Engenharia Naval"}))  
uni.add_department(type("Department", (), {"name": "Engenharia Química"}))  
uni.add_department(type("Department", (), {"name": "Engenharia de Computação"}))  
uni.add_department(type("Department", (), {"name": "Engenharia de Controle e automação"}))  
uni.add_department(type("Department", (), {"name": "Engenharia de Materiais"}))  
uni.add_department(type("Department", (), {"name": "Engenharia de Produção"}))  
uni.add_department(type("Department", (), {"name": "Meteorologia"}))  
uni.add_department(type("Department", (), {"name": "Sistemas de Informação"}))  

print("Departamentos:")
for dept in uni.list_departments():
    print(f"- {dept}")

print(dep.name)
dep.add_teacher(type("Teacher", (), {"name": "Jucimar"}))
dep.add_teacher(type("Teacher", (), {"name": "Elloa"}))
dep.add_teacher(type("Teacher", (), {"name": "Ponciano"}))

for dept in dep.list_teachers():
    print(f"- {dept}")


