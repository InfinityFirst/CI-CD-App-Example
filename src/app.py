from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "First CI-CD Flask app"

if __name__ == '__main__':
    app.run(debug=True)