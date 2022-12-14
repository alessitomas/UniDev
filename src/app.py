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
import pickle
from flask_cors import CORS, cross_origin


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/Unidev.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='unidev', template_mode='bootstrap3')
admin.add_view(ModelView(CursoModel, db.session))
admin.add_view(ModelView(UsuarioModel, db.session))
admin.add_view(ModelView(RespostasModel, db.session))
admin.add_view(ModelView(ExerciciosModel, db.session))


app.config['SECRET_KEY'] = "978FSFHASF8SUHFUAGF789SAGF9AS"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
import os




@app.before_first_request
def create_tables():
    db.create_all()
# apenas reendenização de templates

@app.route('/')
def menu():
    return render_template('landing_page.html')

@app.route('/user')
def form_usuario():
    return render_template('registro.html')


@app.route('/cursos/')
def cursos():

    return render_template('pos_login.html')


@app.route('/logar')
def logar():
    id_user = request.args.get('id_user')
    return render_template('login.html')

@app.route('/code/')
def code():

    return render_template('index.html')

@app.route('/paginafinal/')
def final():
    return render_template('curso_concluido.html')





api.add_resource(Terminal, '/terminal/<string:id_user_ativo>/curso/<string:id_curso_ativo>/')
api.add_resource(Login, '/login/')




@app.route('/terminal/<int:id_user_ativo>/curso/<int:id_curso_ativo>/exercicio/<int:tela>', methods=['POST'])
def salvarexr(id_user_ativo, id_curso_ativo, tela):
    corpo = request.get_json( force=True)
    exr = ExerciciosModel.query.filter_by(id_curso=id_curso_ativo).first()
    print(exr,id_curso_ativo,tela)
    
    resposta = RespostasModel(id_usuario=id_user_ativo, id_curso=id_curso_ativo, tela=tela, resposta=corpo['exr'], id_exercicio=exr.id_exercicio)
    try:
        resposta.save()
        return jsonify({'message': 'salvo com sucesso'}),200
    except:
        return jsonify({'message': 'erro ao salvar'}),500




@app.route('/mudarpg/<int:id_user_ativo>/curso/<int:id_curso_ativo>/exercicio/<int:tela>', methods=['get'])
def mudapg(id_user_ativo, id_curso_ativo, tela):
    curso = CursoModel.query.filter_by(id_curso=id_curso_ativo).first()
    telas = curso.numero_telas
    if tela <= telas:
        ex = ExerciciosModel.query.filter_by(id_curso=id_curso_ativo, tela=tela).first()
        if ex:
            return ex.toDict(),200

        return {'mensagem': "exercício não encontrado"}, 404
    else:
        return {'curso_finalizado': True},200

if __name__ == '__main__':
    db.init_app(app)
    port = os.environ.get("PORT", 5000)
    app.run(debug= False, host="0.0.0.0", port=port)
