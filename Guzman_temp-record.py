from flask import Flask, jsonify, request

import json

app = Flask(__name__)

@app.route('/temp/get', methods=['GET'])
def get_temp():
    with open('temperature.json','r') as f:
        return jsonify(json.load(f))

@app.route('/temp/create', methods=['POST'])
def create_temp():
    with open('temperature.json','r') as f:
        temps = json.load(f)

    temp =  request.get_json()
    temps.append(temp)

    with open('temperature.json','w') as fw:
        json.dump(temps, fw)

    return jsonify(temps),200

@app.route('/temp/<int:id>', methods=['GET'])
def get_tempID(id):
    with open('temperature.json','r') as f:
        temps = json.load(f)
    
    for temp in temps:
        if temp['temp_id'] == id:
            return jsonify(temp),200

@app.route('/temp/update/<int:id>', methods=['POST'])
def update_temp(id):
    with open('temperature.json','r') as f:
        temps = json.load(f)

    for index, temp in enumerate(temps):
        if temp['temp_id'] == id:
            temps[index] = request.get_json()
            break

    with open('temperature.json','w') as fw:
        json.dump(temps, fw)

    return jsonify(temps),200

if __name__ == '__main__':
    app.run()