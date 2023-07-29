import json
from jsonpath_ng import parse
import requests
import sys


def tratativa(obj):
    requisicao = requests.get(f'{obj}')
    data = requisicao.json()
    jsonpath_expr = parse('$.data[*].["auditid"]')
    result = [match.value for match in jsonpath_expr.find(data)]
    lista = [{'{auditid}': result[i]} for i in range(len(result))]
    newValue = [{'{auditid}': lista[x]['{auditid}'], '{resourcename}': data['data'][x]['resourcename']} for x in range(len(data['data']))]
    return newValue
        


if __name__ == "__main__":
    r = tratativa('http://127.0.0.1:8000')
    print(r)
