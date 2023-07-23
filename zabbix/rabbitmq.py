# python 3

import sys
import requests

opc_list = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
protocol = sys.argv[4]
host_api = sys.argv[5]
port = sys.argv[6]

def valor(opc_list):
    match opc_list:
        case 'queue' | 'queue_retry':
            acess_api = requests.get(f"{protocol}://{host_api}:{port}/api/queues", auth=('guest', 'guest'))
            valor = acess_api.json()
            dicionario = dict()
            lista = list()
            for i in valor:
                dicionario["{#NAME}"] = i['name']
                dicionario['{#VHOST}'] = i['vhost']
                lista.append(dicionario.copy())
            print(lista)     
        case 'node':
            acess_api = requests.get(f"{protocol}://{host_api}:{port}/api/overview", auth=('guest', 'guest'))
            valor = acess_api.json()
            node = valor['node']
            print(f'{{"data": [{{"{ "{#NODENAME}"}": "{node}", "{ "{#NODEITEM}"}": "{node[7:]}"}}]}}')
        case 'cluster':
            acess_api = requests.get(f"{protocol}://{host_api}:{port}/api/overview", auth=('guest', 'guest'))
            valor = acess_api.json()
            cluster =  valor['object_totals']
            print(cluster)


valor(opc_list)
