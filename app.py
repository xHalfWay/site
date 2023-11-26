from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Разрешаем все запросы CORS

@app.route('/contact', methods=['POST'])
def save_contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Чтение существующих данных из файла
    try:
        with open('messages.json', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Добавление нового сообщения
    new_message = {'name': name, 'email': email, 'message': message}
    existing_data.append(new_message)

    # Запись обновленных данных в файл
    with open('messages.json', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)

    return jsonify({'success': True, 'message': 'Сообщение успешно сохранено'}), 200

if __name__ == '__main__':
    app.run(debug=True)
