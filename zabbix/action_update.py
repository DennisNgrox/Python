from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://10.10.10.10/")
zapi.login("teste", "pass")

# Obtém todas as ações com suas operações
actions = zapi.action.get({"output": "extend", "selectOperations": "extend"})

# Lista para armazenar os IDs das ações que atendem aos critérios
actions_to_update = []

for action in actions:
    for operation in action['operations']:
        opmessage = operation.get('opmessage')
        if opmessage and opmessage.get('mediatypeid') == '5':
            # Adiciona o ID da ação à lista
            actions_to_update.append(action['actionid'])

# Atualiza cada ação encontrada
for action_id in actions_to_update:
    print(zapi.action.update({
        "actionid": action_id,
        "operations": [
            {
                "operationtype": 0,
                "opmessage": {
                    "default_msg": 0,
                    "message": "Trigger severity: {TRIGGER.SEVERITY} \n TriggerID: {TRIGGER.ID} \n EventID: {EVENT.ID} \n \n Descrição: {EVENT.NAME} \n Host: {HOST.NAME} \n IP: {HOST.CONN} \n Grupo: {TRIGGER.HOSTGROUP.NAME} \n Valor Coletado: \n {ITEM.VALUE} - {TRIGGER.STATUS} \n  Data/Hora do Problema: {ESC.HISTORY} \n\n -- \n Histórico do Item: https://zabbix.sompo.com.br/history.php?&form_refresh=1&itemids%5B0%5D={ITEM.ID}&action=showgraph  \n Gerado por #zabbix em: {DATE}  -  {TIME} \n Acesse o zabbix em https://zabbix.sompo.com.br/"
                },
                "opmessage_grp": [{
                    "usrgrpid": 7
                }]
            }
        ]
    }))

    
