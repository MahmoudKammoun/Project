from flask import Flask, render_template, request
import flask
from flask import request, jsonify,render_template
from historyy import histo
from tasti import nameid
from firefox import aze
import time
from Organisation import orgpack,orgsize
from update_item import subfolder,folder,deel,cre
app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/aa', methods=['GET', 'POST'])
def form():
    return render_template('index.html')

@app.route('/api/action', methods=['GET'])
def api_id():
    if 'path' in request.args:
        if 'id' in request.args:

            id = int(request.args['id'])
            path = str(request.args['path'])
            if id==3:
                subfolder(path)
                time.sleep(20)
                x=orgsize(histo(34797))
                return render_template("index.html", heure = x ,title= "Subfolder Size")
            elif id==4:
                folder(path)
                x=jsonify(orgsize(histo(34797)))
                time.sleep(20)
                return x
            elif id==1:
                 cre(path)
                 time.sleep(30)
                 return jsonify(path+" created")
            elif id==2:
                 deel(path)
                 time.sleep(30)
                 return jsonify(path+" deleted")
        else :
            return "path+ no id"
    else :
        if 'id' in request.args:
            return " id +no path "
        else :
            return "no path + no id"

if __name__ == "__main__":
    app.run()

