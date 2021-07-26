import flask
from flask import request, jsonify
from historyy import histo
from Organisation import api
app = flask.Flask(__name__)
app.config["DEBUG"] = True
item__id =[34792,34793]
@app.route('/api/version/aa', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else :
        return "Error: No id field provided. Please specify an id."


    if  id in item__id:
        xx=api(int(id))
        #print(xx)
        return jsonify(xx)

app.run()

