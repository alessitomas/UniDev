#from flask_login import LoginManager
from crypt import methods
from flask import Flask, request, jsonify, render_template, redirect, url_for
#from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.modelos import CursoModel, UsuarioModel
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import *
from werkzeug.security import generate_password_hash, check_password_hash

from recursos.rotas import Curso, Usuario
from model.sql_alchemy_para_db import db

# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/Unidev.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='unidev', template_mode='bootstrap3')
admin.add_view(ModelView(CursoModel, db.session))
admin.add_view(ModelView(UsuarioModel, db.session))
app.config['SECRET_KEY'] = "978FSFHASF8SUHFUAGF789SAGF9AS"


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


#login_manager = LoginManager()
#login_manager.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# landing page
@app.route('/')
def hello_world():
    return render_template('barros.html')
# register
@app.route('/register', methods =['GET','POST'])
def iniciar_registro():

    if methods == 'POST':
        u = request.form['username']
        p = request.form['password']
        e = request.form['email']
        nome = request.form['nome']


    
    return render_template('register.html')

api.add_resource(Curso, '/curso/<int:id_curso>')
api.add_resource(Usuario, '/usuario/<int:id_usuario>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)