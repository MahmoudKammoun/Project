
#def histo (x):
 #   from pyzabbix import ZabbixAPI
 #   from datetime import datetime
  #  import time
 #   ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
 #   zapi = ZabbixAPI(ZABBIX_SERVER)
 #   zapi.login('Admin', 'zabbix')
 #   timetill = int(time.mktime(time.localtime()))
 #   timefrom = timetill - 30
 #   history = zapi.history.get(itemids=x,
 #                              time_from=timefrom,
 #                              time_till=timetill,
 #                              output='extend',
 #                              limit='5000',
 #                              history=4,
 #                              )

# If nothing was found, try getting it from history (float) data
#    if not len(history):
#        history = zapi.history.get(itemids=x,
                                   #filter={'application': 'others'},
  #                                 time_from=timefrom,
  #                                 time_till=timetill,
 #                                  output='extend',
#                                  limit='5000',
#                                   history=4,
#                                   )
#    for point in history:
#        return(point['value'])
#a=histo(34797)
#print(type(a))

#print(a)
#x=a.find("\n")
#c=a[:x-1]
#print(c)
#print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#z=a[x+1:]
#print(z)
#print(len(a))
#for i in range (0,len(a)+1,a.find("\n")):
#a=a+'\n'

def aze (z):
    dict={}
    i=1
    a=z+"\n"
    while len(a)>2:
        x=a.find("\n")
        dict[str(i)]=a[:x]
        i=i+1
        a=a[x+1:]
    return dict
#print(aze(histo(34797)))
#e="1234567890";
#print(e.find("6"))
#print(e[:e.find("6")])
#print(e[e.find("6")+2:])













#########################################################################
#def mk (x):
#    import subprocess
#    x=str(x)
#    subprocess.check_output(["echo KAMMOUN97 | sudo -S mkdir "+x],shell=True)
#    print(x + " created")
#    return
#def rm (x):
#    import subprocess
#    x=str(x)
#    subprocess.check_output(["echo KAMMOUN97 | sudo -S mkdir "+x],shell=True)
#    print(x + "  deleted")
#    return


#mk("/home/mahmoud/Documents/test1234")
#print(a)
#print(type(a))
#a=str(subprocess.check_output(["mkdir /home/mahmoud/Documents/test5"],shell=True),'utf-8')
    #z="/home/mahmoud/Documents"

