from pyzabbix.api import ZabbixAPI
import sys

zApi = ZabbixAPI(url='http://<ip>/api_jsonrpc.php', user='dennis', password='2023')

hostname = sys.argv[1]

url = hostname.replace("https://", "").replace("http://", "").replace("/","")
hostname = hostname.replace("/","_").replace(".","_").replace(":","").replace("__","_")


create_host = zApi.host.create(
    host = hostname,
    status= 0,
    interfaces=[
        {
        "type": 1,
        "main": "1",
        "useip": 1,
        "ip": '127.0.0.1',
        "dns": "",
        "port": 10050,
        "proxy_hostid": "1" 
        }
    ],
    groups=[
        {
        "groupid": 2
        }
    ]
)

result_create_host = create_host['hostids'][0]


create_http = zApi.httptest.create(
    name = "monitoring",
    hostid = result_create_host,
    steps=[
        {
            "name": "Check_url",
            "url": "http://"+url,
            "status_codes": "200",
            "no": 1
        }
    ]
)

create_trigger = zApi.trigger.create(
    {
        "description": "Falha no webscenario",
        "expression": f"last(/{hostname}/web.test.fail[monitoring])<>0",
        "priority": "4",
        "tags" : [
            {
                "tag": "ticket_action",
                "value": "teste"
            },
            {
                "tag": "monitor_url_incidente",
                "value": "b"
            }
        ]
    }
)


print(create_http)

zApi.user.logout()

