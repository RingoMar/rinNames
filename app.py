from flask import Flask, jsonify, render_template, request, jsonify
from names import rinDerived
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/SomeFunction')
def SomeFunction():
    monkaName = request.args.get('monkaName', default='*', type=str)
    return jsonify(rinDerived().seed_name(monkaName))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
