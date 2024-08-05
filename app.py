from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    # Here you would process the user_message and generate a response
    
    response = {
        'message': f"You said: {user_message}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)