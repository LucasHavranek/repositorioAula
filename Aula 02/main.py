import requests, json, sqlite3

'''res = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/lucas')
print (res.text)'''

'''cep = input("Digite o cep para busca: ")
req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
res = req.json()
print(json.dumps(res, indent=4))'''

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS Alunos (
    matricula integer,
    nome string,
    nota integer
);
''')
conn.commit()

conn.execute("INSERT INTO Alunos VALUES(1, 'Bruno', 5);")
conn.execute("INSERT INTO Alunos VALUES(2, 'Lucas', 5);")
conn.execute("INSERT INTO Alunos VALUES(3, 'Simone', 5);")
conn.execute("INSERT INTO Alunos VALUES(4, 'Mathaeus', 5);")
conn.execute("INSERT INTO Alunos VALUES(5, 'Cássio', 5);")

conn.commit()

#conn.execute("DROP TABLE Alunos")
#conn.commit()

buscar_alunos = conn.execute(
    '''SELECT matricula, nome, nota from Alunos;'''
)

for item in buscar_alunos:
    print(item[0], item[1], item[2])

matricula = input('Informe a matrícula: ')
nome = input('Informe o nome: ')
nota = input('Informe a nota: ')

conn.execute(f"INSERT INTO Alunos VALUES({matricula}, '{nome}', {nota});")
conn.commit()
buscar_alunos = conn.execute('''SELECT matricula, nome, nota from Alunos;''')

for item in buscar_alunos:
    print(item[0], item[1], item[2])