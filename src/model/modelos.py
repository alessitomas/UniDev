from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import *
from model.sql_alchemy_para_db import db
import sqlalchemy


class CursoModel(db.Model):


    id_curso = db.Column(db.Integer, primary_key=True )
    nome_curso = db.Column(db.String(80), nullable = False)
    linguagem = db.Column(db.String(20), nullable = False)


    def __init__(self, id_curso, nome_curso, linguagem):
        self.id_curso = id_curso
        self.nome_curso = nome_curso
        self.linguagem = linguagem

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id': self.id_curso, 'nome':self.nome_curso, 'linguagem':self.linguagem}
    
    def __str__(self):
        return f'{self.nome_curso}'

class UsuarioModel(db.Model):
    _tablename__ = "usuario_model"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    nome = db.Column(db.String(80))
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    senha = db.Column(db.String(20), unique=True)
    def __init__(self,nome, username, email,senha):
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha
        #super(AlunoModel, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def seach_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'nome':self.nome, 'username':self.username, 'email': self.email, 'senha': self.senha}
    
    def __str__(self):
        return f'{self.nome}'


class MatriculaModel(db.Model):


    EM_ABERTO = 0
    CONCLUIDO = 1

    inicio = db.Column(db.DateTime, nullable = False)
    status= db.Column(db.Boolean, default=0)
    fim= db.Column(db.DateTime)
    id_matricula = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer)
    id_curso = db.Column(db.Integer)

    def __init__(self, inicio, status, fim, id_matricula, id_usuario, id_curso):
        self.inicio = inicio
        self.status = status
        self.fim = fim
        self.id_matricula = id_matricula
        self.id_curso = id_curso
        self.id_usuario = id_usuario

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'inicio': self.inicio, 'status':self.status, 'fim':self.fim, 'id matricula':self.id_matricula}

    

class ExerciciosModel(db.Model):


    id_exercicio = db.Column(db.Integer, primary_key=True, nullable = False)

    tela = db.Column(db.Integer)
    pytest = db.Column(db.String(4000))
    titulo = db.Column(db.String(80))
    enunciado = db.Column(db.String(4000), nullable = False)
    gabarito = db.Column(db.String(4000), nullable = False)
    id_curso = db.Column(db.Integer)
    
    def __init__(self, id_exercicio,tela, enunciado, gabarito, pytest, titulo, id_curso):
        self.id_exercicio = id_exercicio
        self.tela = tela
        self.pytest = pytest
        self.titulo = titulo
        self.enunciado = enunciado
        self.gabarito = gabarito
        self.id_curso = id_curso

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id exercicio': self.id_exercicio, 'tela':self.tela, 'enunciado':self.enunciado, 'gabarito':self.gabarito, 'titulo': self.titulo, 'pytest':self.pytest}

class RespostasModel(db.Model):

    resposta = db.Column(db.String(4000), nullable = False)
    id_resposta = db.Column(db.Integer, primary_key = True)
    id_curso = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    id_exercicio = db.Column(db.Integer)
    tela = db.Column(db.Integer)

    def __init__(self, resposta, id_resposta,id_curso,id_usuario,id_exercicio, tela):
        self.resposta = resposta
        self.id_resposta = id_resposta
        self.id_curso = id_curso
        self.id_usuario = id_usuario
        self.id_exercicio = id_exercicio
        self.tela = tela
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id exercicio':self.id_resposta, 'id resposta':self.resposta, 'id curso':self.id_curso, 'id usuario':self.id_usuario, 'id exercicio':self.id_exercicio}