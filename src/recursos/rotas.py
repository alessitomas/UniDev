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


    def post(self):
        corpo = request.get_json( force=True )
        if corpo['senha'] == corpo['senha2']:
            user = UsuarioModel(corpo['nome'], corpo['username'], corpo['email'], corpo['senha']) 
            try:
                user.save()
            except:
                return {"mensagem":"Ocorreu um erro interno ao tentar inserir um curso (DB)"}, 500

            return user.toDict(), 201
        else:
            print('senhas diferentes')
            return {"mensagem": "Senha não confere."}, 401
    
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

    def get(self,id_usuario, id_exercicio):

        #fazer verificacoes sobre curso
        #apresentar enunciado, titulo de acordo com o exercicio

        usuario = UsuarioModel.find_by_id(id_usuario)



        exercicio = ExerciciosModel.find_by_id(id_exercicio)

        if exercicio:
            return exercicio.toDict()

        return {'id': None}, 404

    def post(self, id_exercicio):
        corpo = request.get_json( force=True )

        exercicio = ExerciciosModel(id_exercicio=id_exercicio, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            exercicio.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um exercicio (DB)"}, 500

        return exercicio.toDict(), 201

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

# id_curso, id_usuario
class Terminal(Resource):
    def get(self,id_curso):
        id_usuario=2

        {'titulo':'jdjhshshs'}


        # exercicios = ExerciciosModel.search_all()
        # matriculas = MatriculaModel.search_all()
        # print("teste1")
        # for matricula in matriculas:
        #     if matricula.id_curso == id_curso and matricula.id_usuario == id_usuario:
        #         respostas = RespostasModel.search_all()
        #         lista_tela = []
        #         for resp in respostas:
        #             if resp.id_usuario == id_usuario and resp.id_curso == id_curso:
        #                 lista_tela.append(resp.tela)  #pego a maior tela que ele fez
                
        #         tela_a_fazer = max(lista_tela)+1      #a proxima a ser feita
                
                
        #         for ex in exercicios:
        #             if ex.tela == tela_a_fazer and ex.id_curso == id_curso:
        #                 print("teste2")
        #                 return ex.toDict()

        # for ex in exercicios:
        #     if ex.tela == 1 and ex.id_curso == id_curso:
        #         print("teste2")
        #         return ex.toDict()  
    


    def post(self, id_curso, id_usuario):
        resposta_usuario = request.get_json(force=True)
        resposta = RespostasModel(id_curso=id_resposta) #AlunoModel(corpo['nome'], corpo['numero'])



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
