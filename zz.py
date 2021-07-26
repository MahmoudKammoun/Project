from flask import request, jsonify,render_template
import flask
from histo import zok
app = flask.Flask(__name__)
app.config["DEBUG"] = True
item__id =[34792,34793]
@app.route('/aae', methods=['GET', 'POST'])
def form():
    x=zok()
    return render_template("test.html", result = x)
app.run()
