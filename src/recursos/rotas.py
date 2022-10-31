from flask_restful import Resource
from flask import request, jsonify
import sqlalchemy
from model.modelos import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo






class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senha2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Sign Up')


    

    
class Resposta(Resource):

    def get(self, id_resposta):
        resposta = RespostasModel.find_by_id(id_resposta)

        if resposta:
            return resposta.toDict(),200

        return {'id': None}, 404


    def post(self, id_resposta):
        corpo = request.get_json( force=True )

        resposta = RespostasModel(id_curso=id_resposta, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            resposta.save()
            return {"mensagem":"Usuário criado com sucesso!"},201
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir uma resposta(DB)"}, 500


    def put(self, id_resposta):
        pass
    
    def delete(self, id_resposta):
        resposta = RespostasModel.find_by_id(id_resposta)

        if resposta:
            resposta.delete()
            return {'mensagem': 'Resposta deletado da base.'},202

        return {'mensagem': 'Resposta não encontrada.'}, 404

class Terminal(Resource):
    def get(self,id_user_ativo,id_curso_ativo):
        user = UsuarioModel.query.filter_by(id=id_user_ativo).first()
        curso = CursoModel.query.filter_by(id_curso=id_curso_ativo).first()

        respostas = RespostasModel.search_all()

        exercicios = ExerciciosModel.search_all()
        telas = []
        for resposta in respostas:
            
            if str(resposta.id_curso) == str(id_curso_ativo) and str(resposta.id_usuario) == str(id_user_ativo):
                telas.append(resposta.tela)

        if len(telas) != 0:
            tela_a_fazer = max(telas) + 1
            if int(tela_a_fazer) > int(curso.numero_telas):
                return {'curso_finalizado': True},200

            for ex in exercicios:
                if int(ex.tela) == int(tela_a_fazer) and int(ex.id_curso) == int(id_curso_ativo):
                    return ex.toDict(),200

        else:
            for ex in exercicios:
                print(ex.tela,ex.id_curso)
                print(id_curso_ativo)
                if int(ex.tela) == 1 and int(ex.id_curso) == int(id_curso_ativo):
                    return ex.toDict()


class Login(Resource):
    def get(self):
        pass

    def post(self):

        corpo =request.get_json(force=True)
        user = UsuarioModel.query.filter_by(id=corpo['id_user']).first()
        if user:
            return {'status':True,'id_user':corpo['id_user']}, 200
        else:

            return {'status':False}, 404

    def put(self):
        pass

    def delete(self):
        pass