from flask_restful import Resource
from flask import request, jsonify
import sqlalchemy
from model.modelos import CursoModel, RespostasModel, MatriculaModel, ExerciciosModel


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

class Resposta(Resource):

    def get(self, id_curso):
        resposta = RespostasModel.find_by_id(id_curso)

        if resposta:
            return resposta.toDict()

        return {'id': None}, 404


    def post(self, id_curso, id_user):
        corpo = request.get_json( force=True )

        resposta = RespostasModel(id_curso=id_curso, id_user=id_user, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            resposta.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir uma resposta(DB)"}, 500

        return resposta.toDict(), 201

    def put(self, id_curso):
        pass
    
    def delete(self, id_curso):
        resposta = RespostasModel.find_by_id(id_curso)

        if resposta:
            resposta.delete()
            return {'mensagem': 'Resposta deletado da base.'}

        return {'mensagem': 'Resposta não encontrada.'}, 404

class Matricula(Resource):

    def get(self, id_curso):
        resposta = MatriculaModel.find_by_id(id_curso)

        if resposta:
            return resposta.toDict()

        return {'id': None}, 404

    def post(self, id_curso, id_user):
        corpo = request.get_json( force=True )

        matricula = MatriculaModel(id_curso=id_curso, id_user=id_user, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            matricula.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir uma matricula (DB)"}, 500

        return matricula.toDict(), 201

    def put(self, id_curso):
        pass

    def delete(self, id_curso):
        resposta = RespostasModel.find_by_id(id_curso)

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

        matricula = MatriculaModel(id_curso=id_exercicio, id_user=id_exercicio, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
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
    