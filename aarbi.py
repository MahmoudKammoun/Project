from historyy import histo
import flask
from flask import request, jsonify
a= (histo(34791))
C=a.find('\n')
b=a[: a.find("apache2")+len("apache2")]
b=b+'\n'
print(b)
list=[]
#z=True
while len(b)>0 :
    c=b.find('\n')
    list.append(b[0:c-1])
    b=b[c:]



print(list)

#print (type(histo(34791)))
#app = flask.Flask(__name__)
#app.config["DEBUG"] = True
#@app.route('/api/package', methods=['GET'])
#def api_package():
#    return jsonify(a)
#app.run()
