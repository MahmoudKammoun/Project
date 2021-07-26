import json
import os
import sys

import flask
from File import create_file
from toporg import orgnaize
from flask import request, jsonify,redirect,render_template
from historyy import histo,histoo,histooo
from tasti import nameid,nameid_host
import time
from updatexml import add_command,delete_command,update_command,delete_commandid
from Organisation import orgpack,orgsize
from update_item import subfolder,folder,deel,cre
from universal import universalCL
from Create_item import item_create
from add import getname,getCL
from histo import list_host
app = flask.Flask(__name__)
app.config["DEBUG"] = True
item__id =[34792,34793]
#x=getname()
#cl=getCL()
@app.route('/', methods=['GET', 'POST'])
def home():
    x=list_host()

    return render_template("index.html", result = x,memory=histoo(34474),space=histoo(34557),cpu=histoo(34473))

@app.route('/aa', methods=['GET','POST'])
def form():

        return render_template('login.html')
@app.route('/aa/3', methods=['GET'])
def forme():
    l=list_host()
    p=1
    imp=1
    a={}
    b={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1
    #print(l)
    return render_template('najd2.html',y=getname("command.xml"),result=l,p=a,imp=b)

@app.route('/api/action', methods=['GET','POST'])
def api_id():
    l={}
    host_id=request.args.getlist("host")
    id = int(request.args['id'])
    for i in range (len(host_id)):
            l[str(i+1)]=str(host_id[i])

    #print(type(host_id))
    if id==3:
        path = str(request.args['path'])
        k={}
        for i in range (len(l)):

            subfolder(path,l[str(i+1)])

            w=orgsize(histo(str(nameid("folder size",nameid_host(l[str(i+1)])))))
            k[l[str(i+1)]]=w
        #return k
        return render_template("indexxx.html", result = w ,res=k, title= "Subfolder Size",type="SubFolder",the=host_id)
    elif id==4:
        path = str(request.args['path'])
        folder(path,host_id)
        x=orgsize(histo(str(nameid("folder size",nameid_host(host_id)))))
        time.sleep(20)
        return render_template("indexx.html", result = x , title= "Folder Size",type="Folder",memory=histoo(34474),space=histoo(34557),cpu=histoo(34473),the=host_id)
    elif id==1:
        path = str(request.args['path'])
        cre(path,host_id)
        time.sleep(30)
        return render_template("action.html", result = path, title= "Creation of a folder",memory=histoo(34474),space=histoo(34557),cpu=histoo(34473),the=host_id)
    elif id==2:
        path = str(request.args['path'])
        deel(path,host_id)
        time.sleep(30)
        return render_template("action_del.html", result = path, title= "Deletion of a folder",memory=histoo(34474),space=histoo(34557),cpu=histoo(34473),the=host_id)
    elif id==5:
        path = str(request.args['path'])
        id2=nameid(path,host_id)
        x=orgpack(histo(id2))
        return render_template("action_version.html", result = x,title= "Version of a Package",memory=histoo(34474),space=histoo(34557),cpu=histoo(34473),the=host_id)
    elif id == 6:
        path = str(request.args['path'])
        return render_template("top.html", v= orgnaize(34798))
    else:
        universalCL(getCL("command.xml")[str(id)])
        a=histo(34810)
        path = str(request.args['path'])

        return render_template("terminal.html",result=a,path=host_id)

#@app.route('/api/version', methods=['GET'])
#def api1_id():
#    if 'name' in request.args:
#        name = str(request.args['name'])
#        id=nameid(name)

#    else :
#        return "Error: No id field provided. Please specify an id."


#    if  id in item__id:
#        xx=orgpack(histo(id))
        #print(xx)
 #       return jsonify(xx)

@app.route('/aa/1', methods=['GET','POST'])
def data():

   return render_template("add.html")
@app.route('/aa/2', methods=['GET','POST'])
def handle_data():
    id = request.form['id']
    name=request.form['name']
    script = request.form['script']

    add_command(str(name),str(script),str(id))

    #time.sleep(5)
    #getname()[id]= script
    o=list_host()
    #json.dump(naj,open("out.json","w"))
    #getname().update()

    #create_file(str(id),str(script))
    #item_create(id)
    #data
    #def aa():
    #    return render_template("naj.html", y=getname(), result=o)

    #time.sleep(10)
    #print("####################")
    #return os.execv(sys.executable,['python']+sys.argv)
    l=list_host()
    p=1
    imp=1
    a={}
    b={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1
    return render_template('najd2.html',y=getname("command.xml"),result=l,p=a,imp=b)

#@app.route('/api/version', methods=['GET'])
#def api1_id():
#    if 'name' in request.args:
#        name = str(request.args['name'])
#        id=nameid(name)

#    else :
#        return "Error: No id field provided. Please specify an id."


#    if  id in item__id:
#        xx=orgpack(histo(id))
        #print(xx)
 #       return jsonify(xx)
@app.route('/aa/delete', methods=['GET'])
def delete():

   return render_template("delete.html",result=getname("command.xml"))
@app.route('/aa/delete', methods=['POST'])
def handle_dataa():
    n = request.form['root']
    name=str(n)
    delete_command(name)
    z=name+" was deleted"


    return render_template("delete.html",result=getname("command.xml"))
@app.route('/aa/update', methods=['GET'])
def update():

   return render_template("update.html",result=getname("command.xml"))
@app.route('/aa/update/1', methods=['POST'])
def handle_dataaa():
    n = request.form['root']
    tuple=update_command("command.xml",n)



    return render_template("update_1.html",id=tuple[0],name=tuple[1],script=tuple[2])
@app.route('/aa/update/2', methods=['GET','POST'])
def handle_dat():
    id = request.form['id']
    name=request.form['name']
    script = request.form['script']
    delete_commandid(str(id))
    add_command(str(name),str(script),str(id))
    o=list_host()
    l=list_host()
    p=1
    imp=1
    a={}
    b={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1

    return render_template('najd2.html',y=getname("command.xml"),result=l,p=a,imp=b)

app.templates_auto_reload=True
app.run()
