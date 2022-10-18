#from flask_login import LoginManager
from flask import Flask, request, jsonify, render_template, redirect, url_for
#from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.modelos import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import *
from werkzeug.security import generate_password_hash, check_password_hash
from recursos.rotas import *
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
admin.add_view(ModelView(MatriculaModel, db.session))
admin.add_view(ModelView(ExerciciosModel, db.session))
admin.add_view(ModelView(RespostasModel, db.session))
app.config['SECRET_KEY'] = "978FSFHASF8SUHFUAGF789SAGF9AS"
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

@app.route('/usuario/adicionar', methods=['POST', 'GET'])
def adicionar_usuario():
    nome = None
    form = UserForm()
    if form.validate_on_submit():
        user = UsuarioModel.query.filter_by(email=form.email.data).first()
        if user is None:
            senha_hashed = generate_password_hash(form.senha.data, 'sha256')
            user = UsuarioModel(nome=form.nome.data, username=form.username.data, email=form.email.data, senha = senha_hashed)
            db.session.add(user)
            db.session.commit()
            nome = form.nome.data
            form.nome.data = ''
            form.username.data = ''
            form.email.data = ''
            form.senha.data = ''
        return render_template('src\templates\add_user.html', nome=nome, form=form)
    return 'OI'
     
api.add_resource(Curso, '/curso/<int:id_curso>')
api.add_resource(Matricula, '/usuario/<int:id_usuario>/<int:id_matricula>')
api.add_resource(Exercicio, '/curso/<int:id_curso>/<int:id_exercicio>')
api.add_resource(Resposta, '/curso/<int:id_curso>/<int:id_resposta>')
api.add_resource(Usuario, '/usuario/<int:id_usuario>')



if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)