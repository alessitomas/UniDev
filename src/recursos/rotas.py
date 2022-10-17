from flask_restful import Resource
from flask import request, jsonify
import sqlalchemy
from model.modelos import *
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


