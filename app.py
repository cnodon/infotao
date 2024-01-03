from flask import Flask, render_template, request,jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clipboard', methods=['POST'])
def clipboard():
    data = request.data.decode('utf-8')
    return data

@app.route('/chatWithModel', methods=['POST'])
def call_python_function():
    data = request.get_json()
    result = chatWith(data)
    return jsonify(result)

def chatWith(data):
    # Your Python function here
    return {"result": "This is the result from my_python_function"}


if __name__ == '__main__':
    app.run(debug=True)