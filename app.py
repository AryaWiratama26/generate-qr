from flask import Flask, render_template
from sources.generate import generate_qr

data = generate_qr("https://indonesia.com", "indonesia")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)