#from flask_login import LoginManager
from flask import Flask, request, jsonify
#from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.modelos import CursoModel, RespostasModel
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from recursos.rotas import Curso
from model.sql_alchemy_para_db import db

# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/cursos.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
app.secret_key = '3c6v5n' 
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='unidev', template_mode='bootstrap3')
admin.add_view(ModelView(CursoModel, db.session))
admin.add_view(ModelView(RespostasModel, db.session))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


#login_manager = LoginManager()
#login_manager.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def hello_world():
    return f"<p>Hello, World!</p>"

@app.route('/teste')
def teste():
    t = CursoModel(1,'teste','python')
    t.save()

api.add_resource(Curso, '/curso/<int:id_curso>')

@app.route('/teste2')
def teste2():
    t = RespostasModel(1,1,'resposta teste')
    t.save()

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)