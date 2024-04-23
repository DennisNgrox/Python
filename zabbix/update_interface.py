from zabbix_api import ZabbixAPI


arquivo = open("C:\\Users\\Ageri\\Desktop\\hosts_update")
lista = []
for name in arquivo:
    lista.append(name.split("\n"))


zapi = ZabbixAPI(server="http://ip/api_jsonrpc.php")
zapi.login("Admin", "adm")

for i in lista:
    name = i[0]
    hosts = zapi.host.get({
        "output": ["hostid", "host"],
        "selectInterfaces": ["port", "interfaceid"],
        "filter": {
            "port": "10050"
        },
        "search": {
            "host": name
        }       
    })

    print(hosts)

    if not hosts:
        print(f"Não encontrou o host {name}")
    else:
        print(f'Host {name} encontrado, seguindo tratativa de update')
        for i in hosts:
            name = i["host"]
            hid = i["hostid"]
            iid = i["interfaces"][0]["interfaceid"]
            hosts_update = zapi.hostinterface.update({
                "interfaceid": iid,
                "port": 10052
            })

        for i in hosts:
            hid = i["hostid"]
            hosts_update_enable = zapi.host.update({
                "hostid": hid,
                "status": 0
            })

    
