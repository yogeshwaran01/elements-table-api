from flask import Flask, jsonify, request

app = Flask(__name__)

def data_list():
    import csv
    file = open("table.csv")
    data_dict = csv.DictReader(file)
    dict_list = [0]
    for line in data_dict:
        dict_list.append(line)
    return dict_list

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '404 Not Found'}), 404

@app.route("/")
def all():
    return jsonify(data_list())

@app.route("/<num>")
def atomic_number(num):
    try:
        return jsonify([data_list()[int(num)]])
    except:
        return not_found(404)
    
@app.route("/name")
def elements():
    _list = []
    for i in data_list()[1:]:
        _list.append(i[" name"])
    return jsonify(_list)

@app.route("/name/<name>")
def by_element_name(name):
    _list = []
    for i in data_list()[1:]:
        if i[" name"].strip().lower() == name:
            _list.append(i)
        else:
            continue
    if len(_list) == 0:
        return not_found(404)
    else:
        return jsonify(_list)

@app.route("/symbol")
def symbol():
    _list = []
    for i in data_list()[1:]:
        _list.append(i[" symbol"])
    return jsonify(_list)

@app.route("/symbol/<symbol>")
def by_symbol(symbol):
    _list = []
    for i in data_list()[1:]:
        if i[" symbol"].strip() == symbol:
            _list.append(i)
        else:
            continue
    if len(_list) == 0:
        return not_found(404)
    else:
        return jsonify(_list)


if __name__ == "__main__":
    app.run()
