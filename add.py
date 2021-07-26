import xml.etree.cElementTree as et


def getname(x):
    tree=et.parse(str(x))
    root=tree.getroot()
    name=[]
    id=[]
    dict={}

    for time in root.iter('name'):
        name.append(time.text)

    for idd in root.iter('id'):
        id.append(idd.text)

    for i in range (len(id)):
        dict[str(id[i])]=name[i]

    return dict
#print(getname())
def getCL(x):
    tree=et.parse(x)
    root=tree.getroot()
    CL=[]
    id=[]
    dict={}
    for time in root.iter('content'):
        CL.append(time.text)

    for idd in root.iter('id'):
        id.append(idd.text)

    for i in range (len(id)):
        dict[str(id[i])]=CL[i]
    return dict
#print(getCL())
#print("#############")
#print(getname())
