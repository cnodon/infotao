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
    
    return 

def chatWith(data):
    # Your Python function here
    return {"result": "This is the result from chatWithModel"}


if __name__ == '__main__':
    app.run(debug=True)