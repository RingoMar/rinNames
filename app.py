from flask import Flask, jsonify, render_template, request, jsonify
from main import rinDerived
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/SomeFunction')
def SomeFunction():
    monkaName = request.args.get('monkaName', default='*', type=str)
    return jsonify(rinDerived().seed_name(monkaName))


if __name__ == '__main__':
    app.run()
