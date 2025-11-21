from flask import Flask, render_template, request
from sources import generate_qr


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data_res = None
    if request.method == 'POST':
        get_link = request.form.get('link')
        get_nama = request.form.get('nama')

        generate_qr(get_link, get_nama)
        data_res = get_nama

    return render_template('index.html', data_res=data_res)


if __name__ == '__main__':
    app.run(debug=True, port=1245)