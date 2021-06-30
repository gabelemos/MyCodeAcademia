import json

#funcion to read the JSON file
def ler_json():
    with open('tabela.json', 'r', encoding='utf8') as c:
        return json.load(c)

#putting the JSON file read in a variable
myjson = ler_json()

#print(myjson[0]['modelos'][0]['nome'])
#print(myjson[0].get("modelos"))
#list.append(ler_json())

#part the lists of objects in JSON file
lista_carros = [myjson[0]["modelos"][0]['nome'],
                myjson[0]["modelos"][1]['nome'],
                myjson[0]["modelos"][2]['nome'],
                myjson[0]["modelos"][3]['nome'],]

lista_personagens = [myjson[1]["modelos"][0]['nome'],
                     myjson[1]["modelos"][1]['nome'],
                     myjson[1]["modelos"][3]['nome'],
                     myjson[1]["modelos"][2]['nome']]

anosdefabrica = ('-------------------------\nNome: {}\nAno de Fabricação: {}'.format(myjson[0]["modelos"][0]['nome'], myjson[0]["modelos"][0]['ano']))
anosdefabrica2 = ('-------------------------\nNome: {}\nAno de Fabricação: {}'.format(myjson[0]["modelos"][1]['nome'], myjson[0]["modelos"][1]['ano']))
anosdefabrica3 = ('-------------------------\nNome: {}\nAno de Fabricação: {}'.format(myjson[0]["modelos"][2]['nome'], myjson[0]["modelos"][2]['ano']))
anosdefabrica4 = ('-------------------------\nNome: {}\nAno de Fabricação: {}\n-------------------------'.format(myjson[0]["modelos"][3]['nome'], myjson[0]["modelos"][3]['ano']))


estado_fabricado = ('-------------------------\nNome: {}\nEstado de fabricação: {}'.format(myjson[0]["modelos"][0]['nome'], myjson[0]["modelos"][0]['em_fabricacao']))
estado_fabricado2 = ('-------------------------\nNome: {}\nEstado de fabricação: {}'.format(myjson[0]["modelos"][1]['nome'], myjson[0]["modelos"][1]['em_fabricacao']))
estado_fabricado3 = ('-------------------------\nNome: {}\nEstado de fabricação: {}'.format(myjson[0]["modelos"][2]['nome'], myjson[0]["modelos"][2]['em_fabricacao']))
estado_fabricado4 = ('-------------------------\nNome: {}\nEstado de fabricação: {}\n-------------------------'.format(myjson[0]["modelos"][3]['nome'], myjson[0]["modelos"][3]['em_fabricacao']))

idades0 = '-------------------------\nNome: {}\nIdade: {}'.format(myjson[1]["modelos"][0]['nome'],  2021 - myjson[1]["modelos"][0]['ano'])
idades1 = '-------------------------\nNome: {}\nIdade: {}'.format(myjson[1]["modelos"][1]['nome'],  2021 - myjson[1]["modelos"][1]['ano'])
idades2 = '-------------------------\nNome: {}\nIdade: {}'.format(myjson[1]["modelos"][2]['nome'],  2021 - myjson[1]["modelos"][2]['ano'])
idades3 = '-------------------------\nNome: {}\nIdade: {}\n-------------------------'.format(myjson[1]["modelos"][3]['nome'],  2021 - myjson[1]["modelos"][3]['ano'])

sexo0 = '-------------------------\nNome: {}\nSexo: {}'.format(myjson[1]["modelos"][0]['nome'], myjson[1]["modelos"][0]['sexo'])
sexo1 = '-------------------------\nNome: {}\nSexo: {}'.format(myjson[1]["modelos"][1]['nome'], myjson[1]["modelos"][1]['sexo'])
sexo2 = '-------------------------\nNome: {}\nSexo: {}'.format(myjson[1]["modelos"][2]['nome'], myjson[1]["modelos"][2]['sexo'])
sexo3 = '-------------------------\nNome: {}\nSexo: {}\n-------------------------'.format(myjson[1]["modelos"][3]['nome'], myjson[1]["modelos"][3]['sexo'])

estudando0 = '-------------------------\nNome: {}\nEstudando: {}'.format(myjson[1]["modelos"][0]['nome'], myjson[1]["modelos"][0]['estudando'])
estudando1 = '-------------------------\nNome: {}\nEstudando: {}'.format(myjson[1]["modelos"][1]['nome'], myjson[1]["modelos"][1]['estudando'])
estudando2 = '-------------------------\nNome: {}\nEstudando: {}'.format(myjson[1]["modelos"][2]['nome'], myjson[1]["modelos"][2]['estudando'])
estudando3 = '-------------------------\nNome: {}\nEstudando: {}\n-------------------------'.format(myjson[1]["modelos"][3]['nome'], myjson[1]["modelos"][3]['estudando'])

#lista_fabricacao = [myjson[0]["modelos"]['nome'], [myjson[0]["modelos"][0]['em_fabricacao']]]
#Here, the users choose one list to see

escolha = input(str('Qual lista deseja ver? \n1 - Carros\n2 - Personagens\n'))

if escolha == '1':
    escolha_1 = (input(str('Deseja ver: \n1 - Ano de Fabricação\n2 - Estado de Fabricação\n')))
    if escolha_1 == '1':
        print(anosdefabrica)
        print(anosdefabrica2)
        print(anosdefabrica3)
        print(anosdefabrica4)
    escolha_1 = (input(str('Deseja ver: \n1 - Ano de Fabricação\n2 - Estado de Fabricação\n')))
    if escolha_1 == '2':
        print(estado_fabricado)
        print(estado_fabricado2)
        print(estado_fabricado3)
        print(estado_fabricado4)
    escolha = input(str('Qual lista deseja ver? \n1 - Carros\n2 - Personagens\n'))
if escolha == '2':
    escolha_2 = (input(str('Deseja ver: \n1 - Idade\n2 - Sexo\n3 - Estudando\n')))
    if escolha_2 == '1':
        print(idades0)
        print(idades1)
        print(idades2)
        print(idades3)
    escolha_2 = (input(str('Deseja ver: \n1 - Idade\n2 - Sexo\n3 - Estudando\n')))
    if escolha_2 == '2':
        print(sexo0)
        print(sexo1)
        print(sexo2)
        print(sexo3)
    escolha_2 = (input(str('Deseja ver: \n1 - Idade\n2 - Sexo\n3 - Estudando\n')))
    if escolha_2 == '3':
        print(estudando0)
        print(estudando1)
        print(estudando2)
        print(estudando3)