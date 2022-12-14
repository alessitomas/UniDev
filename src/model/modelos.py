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
    numero_telas = db.Column(db.Integer)    


    def __init__(self, id_curso, nome_curso, linguagem, numero_telas):
        self.id_curso = id_curso
        self.nome_curso = nome_curso
        self.linguagem = linguagem
        self.numero_telas = numero_telas

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



class ExerciciosModel(db.Model):


    id_exercicio = db.Column(db.Integer, primary_key=True, nullable = False)

    tela = db.Column(db.Integer)
    pytest = db.Column(db.String(4000))
    titulo = db.Column(db.String(80))
    enunciado = db.Column(db.String(4000), nullable = False)

    id_curso = db.Column(db.Integer)
    
    def __init__(self, id_exercicio,tela, enunciado, pytest, titulo, id_curso):
        self.id_exercicio = id_exercicio
        self.tela = tela
        self.pytest = pytest
        self.titulo = titulo
        self.enunciado = enunciado
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
        return {'id exercicio': self.id_exercicio, 'tela':self.tela, 'enunciado':self.enunciado, 'titulo': self.titulo, 'pytest':self.pytest}

class RespostasModel(db.Model):

    id_resposta = db.Column(db.Integer, primary_key=True, autoincrement = True )
    id_curso = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    id_exercicio = db.Column(db.Integer)
    resposta = db.Column(db.String(4000))
    tela = db.Column(db.Integer)

    def __init__(self,id_curso,id_usuario,id_exercicio,resposta,tela):

        self.id_curso = id_curso
        self.id_usuario = id_usuario
        self.id_exercicio = id_exercicio
        self.resposta = resposta
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