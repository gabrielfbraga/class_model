from university import university

# criando uma instância da classe University
uni = university("Escola Superior de Tecnologia", "Amazonas")

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
