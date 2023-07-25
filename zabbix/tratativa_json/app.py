import json
f = open('audit.log', 'r')
dt = json.loads(f.read())
data = dt['result']

lista = [{'auditid' : i['auditid'], 'details' : i['details']} for i in data]

# dicionario = {}
# lista = []
# for i in data:
#     dicionario['auditid'] = i['auditid']
#     lista.append(dicionario.copy())

print(lista)




