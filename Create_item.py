from pyzabbix import ZabbixAPI
ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin', 'zabbix')
#timetill = int(time.mktime(time.localtime()))
#timefrom = timetill - 30
def item_create(id_name):
    zapi.item.create(name=str(id_name)+".py",
                     key_="run["+str(id_name)+".py]",
                     hostid="10396",
                     type=0,
                     delay="30s",
                     value_type=4,
                     interfaceid="6"
                    )
    return
#history= zapi.hostinterface.get(output="extend",
#                                hostids="10396")
#print(history)

