from flask import Flask, jsonify, request

contacts = [
    {
        'id': 1,
        'name': 'test',
        'contact': '000',
    }
]

app = Flask(__name__)

@app.route('/add-contacts', methods=['POST'])
def add_contacts():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'please add a contact'
        })

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json['contact']
    }

    contacts.append(contact)

    return jsonify({
        'status': 'success',
        'message': 'contact successfully created'
    })

@app.route('/get-contacts')
def get_contacts():
    return jsonify({
        'data': contacts
    })

if __name__ == '__main__':
    app.run()