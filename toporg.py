from historyy import histo
def orgnaize(x):
    a=(histo(x))

    #print(a.rfind(":"))
    b=a.rfind(":")
    #print(len(a))
    mem=(a[b-7: b-4])
    cpu=(a[b-13:b-9])

    dict={'memory  utilisation %':str(mem),"CPU utilisation %":str(cpu)}
    return dict
#print(orgnaize(34798))
#34798
