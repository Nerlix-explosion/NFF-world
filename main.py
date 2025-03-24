"""
from flask import Flask, request, jsonify
from StonehengeCalc import calc
app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])  # Разрешаем оба метода для тестирования
def api():
    try:
        if request.method == 'GET':
            data = request.args.to_dict()  # Для GET-параметров
        else:
            data = request.get_json()  # Для POST с JSON

        # Проверяем обязательные поля
        required_fields = ['year', 'month', 'day']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Устанавливаем значения по умолчанию для часа и минуты
        hour = data.get('hour', '0')
        minute = data.get('minute', '0')

        # Вычисляем данные
        sun_data = calc('1', data['year'], data['month'], data['day'], hour, minute)
        moon_data = calc('2', data['year'], data['month'], data['day'], hour, minute)
        sunrise_data = calc('3', data['year'], data['month'], data['day'])
        sunset_data = calc('4', data['year'], data['month'], data['day'])

        # Формируем ответ
        response = {
            "sun": sun_data,
            "moon": moon_data,
            "sunrise": sunrise_data,
            "sunset": sunset_data
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
"""
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])  # Разрешаем оба метода для тестирования
def api():
    try:
        if request.method == 'GET':
            data = request.get_json()
             # Для GET-параметров
        else:
            data = request.args.to_dict() 
    except:
        return "ERROR"
    response = []
    return jsonify(response)
