from flask_restful import Resource
from flask import request, jsonify
import sqlalchemy
from model.modelos import CursoModel, MatriculaModel, ExerciciosModel, UsuarioModel, RespostasModel
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo



class Curso(Resource):

    def get(self, id_curso):
        curso = CursoModel.find_by_id(id_curso)

        if curso:
            return curso.toDict()

        return {'id': None}, 404


    def post(self, id_curso):
        corpo = request.get_json( force=True )

        curso = CursoModel(id_curso=id_curso, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            curso.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um curso (DB)"}, 500

        return curso.toDict(), 201

    def put(self, id_curso):
        pass
    
    def delete(self, id_curso):
        curso = CursoModel.find_by_id(id_curso)

        if curso:
            curso.delete()
            return {'mensagem': 'Curso deletado da base.'}

        return {'mensagem': 'Curso não encontrado.'}, 404

class Usuario(Resource):

    def get(self, id_usuario):
        user = UsuarioModel.find_by_id(id_usuario)

        if user:
            return user.toDict()

        return {'id': None}, 404


    def post(self, id_usuario):
        corpo = request.get_json( force=True )

        user = UsuarioModel(id_usuario=id_usuario, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            user.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um curso (DB)"}, 500

        return user.toDict(), 201

    def put(self, id_usuario):
        pass
    
    def delete(self, id_usuario):
        user = UsuarioModel.find_by_id(id_usuario)

        if user:
            user.delete()
            return {'mensagem': 'Curso deletado da base.'}

        return {'mensagem': 'Curso não encontrado.'}, 404

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senha2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Sign Up')


class Matricula(Resource):

    def get(self, id_matricula):
        resposta = MatriculaModel.find_by_id(id_matricula)

        if resposta:
            return resposta.toDict()

        return {'id': None}, 404

    def post(self, id_matricula):
        corpo = request.get_json( force=True )

        matricula = MatriculaModel(id_curso=id_matricula, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            matricula.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir uma matricula (DB)"}, 500

        return matricula.toDict(), 201

    def put(self, id_matricula):
        pass

    def delete(self, id_matricula):
        resposta = MatriculaModel.find_by_id(id_matricula)

        if resposta:
            resposta.delete()
            return {'mensagem': 'Resposta deletado da base.'}

        return {'mensagem': 'Resposta não encontrada.'}, 404
    
class Exercicio(Resource):

    def get(self, id_exercicio):
        exercicio = ExerciciosModel.find_by_id(id_exercicio)

        if exercicio:
            return exercicio.toDict()

        return {'id': None}, 404

    def post(self, id_exercicio):
        corpo = request.get_json( force=True )

        matricula = MatriculaModel(id_exercicio=id_exercicio, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            matricula.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um exercicio (DB)"}, 500

        return matricula.toDict(), 201

    def put(self, id_exercicio):
        pass

    def delete(self, id_exercicio):
        exercicio = ExerciciosModel.find_by_id(id_exercicio)

        if exercicio:
            exercicio.delete()
            return {'mensagem': 'Exercicio deletado da base.'}

        return {'mensagem': 'Exercicio não encontrado.'}, 404
    
class Resposta(Resource):

    def get(self, id_resposta):
        resposta = RespostasModel.find_by_id(id_resposta)

        if resposta:
            return resposta.toDict()

        return {'id': None}, 404


    def post(self, id_resposta):
        corpo = request.get_json( force=True )

        resposta = RespostasModel(id_curso=id_resposta, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            resposta.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir uma resposta(DB)"}, 500

        return resposta.toDict(), 201

    def put(self, id_resposta):
        pass
    
    def delete(self, id_resposta):
        resposta = RespostasModel.find_by_id(id_resposta)

        if resposta:
            resposta.delete()
            return {'mensagem': 'Resposta deletado da base.'}

        return {'mensagem': 'Resposta não encontrada.'}, 404