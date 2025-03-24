from flask import Flask, request, jsonify
from StonehengeCalc import calc
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # Получаем 3 параметра из URL
    context = []
    data = request.get_json()
    modes1 = ['Sun', 'Moon']
    modes2 = ['Sunrise', 'Sunset']

    # Проверяем наличие всех полей
    if not data or not all(key in data for key in ['year']):
        return jsonify({"error": "Missing or invalid JSON data"}), 400

    y = data['year']
    mt = data['month']
    d = data['day']
    h = data['hour']
    m = data['minute']

    data1 = calc(str(modes1.index(modes1[0])+1), y, mt, d, h, m)
    data2 = calc(str(modes1.index(modes1[1])+1), y, mt, d, h, m)
    data3 = calc(str(len(modes1)+modes2.index(modes2[0])+1), y, mt, d)
    data4 = calc(str(len(modes1)+modes2.index(modes2[1])+1), y, mt, d)
    context = {**context, **data1, **data2, **data3, **data4}
    # Ваша логика обработки (например, просто возвращаем их)

    return jsonify(context)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
