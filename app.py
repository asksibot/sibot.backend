from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    return jsonify({"reply": "Here's a response from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
