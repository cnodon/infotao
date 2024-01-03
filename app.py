from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clipboard', methods=['POST'])
def clipboard():
    data = request.data.decode('utf-8')
    return data

if __name__ == '__main__':
    app.run(debug=True)