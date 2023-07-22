from pyzabbix.api import ZabbixAPI

zApi = ZabbixAPI(url='http://<ip>/api_jsonrpc.php', user='Admin', password='zabbix')

result =  zApi.host.create(
    host = 'hostname',
    status= 1,
    interfaces=[{
        "type": 1,
        "main": "1",
        "useip": 1,
        "ip": '127.0.0.1',
        "dns": "",
        "port": 10050
    }],
    groups=[{
        "groupid": 2
    }],
    templates=[{
        "templateid": 10001
    }])


print(result)

zApi.user.logout()
