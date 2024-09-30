from flask import Flask, render_template, request # redirect, url_for
from model import add_senha, senhas, delete_senha

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', senhas = senhas)

@app.route('/', methods=['POST'])
def add():
    add_senha(request.form["senha"])
    return render_template('index.html', senhas = senhas)

@app.route('/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    delete_senha(id)
    return render_template('index.html', senhas = senhas)
# redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
