from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import *
from model.sql_alchemy_para_db import db
import sqlalchemy


class CursoModel(db.Model):
    _tablename__ = "curso_model"

    id_curso = db.Column(db.Integer, primary_key=True )
    nome_curso = db.Column(db.String(80))
    linguagem = db.Column(db.String(20))
    #exercicios = db.relationship('ExerciciosModel', secondary="exercicios_model", backref='curso_exercicios') 

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
        return {'id': self.id, 'nome':self.nome, 'linguagem':self.linguagem}



class MatriculaModel(db.Model):
    _tablename__ = "matricula"

    EM_ABERTO = 1
    CONCLUIDO = 0

    id_user = db.Column(db.ForeignKey(UsuarioModel.id_usuario), nullable=False)
    id_curso = db.Column(db.ForeignKey(CursoModel.id_curso), nullable=False)
    inicio = db.Column(db.DateTime)
    status= db.Column(db.Boolean, default=1)
    fim= db.Column(db.DateTime)
    ##exercicios = db.relationship('CursoModel', secondary="curso_model", backref='exercicios_curso') 

    def __init__(self, id_user, id_curso, inicio, status, fim):
        self.id_curso = id_curso
        self.id_user = id_user
        self.inicio = inicio
        self.status = status
        self.fim = fim

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
        return {'id user': self.id_user, 'id curso':self.id_curso, 'inicio':self.inicio, 'status':self.status, 'fim':self.fim}

class ExerciciosModel(db.Model):
    _tablename__ = "exercicios_model"

    id_exercicio = db.Column(db.Integer, primary_key=True)
    id_curso = db.Column(db.ForeignKey(CursoModel.id_curso), nullable=False)
    tela = db.Column(db.Integer)
    #pytest 
    enunciado = db.Column(db.String(4000), nullable = False)
    gabarito = db.Column(db.String(4000), nullable = False)

    ##exercicios = db.relationship('CursoModel', secondary="curso_model", backref='exercicios_curso') 

    def __init__(self, id_exercicio, id_curso, tela, enunciado, gabarito):
        self.id_exercicio = id_exercicio
        self.id_curso = id_curso
        self.tela = tela
        self.enunciado = enunciado
        self.gabarito = gabarito

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
        return {'id exercicio': self.id_exercicio, 'id curso':self.id_curso, 'tela':self.tela, 'enunciado':self.enunciado, 'gabarito':self.gabarito}

class RespostasModel(db.Model):
    _tablename__ = "respostas_model"

    id_usuario = db.Column(db.ForeignKey(UsuarioModel.id_usuario), nullable=False)
    id_exercicio = db.Column(db.ForeignKey(ExerciciosModel.id_exercicio), nullable=False)
    resposta = db.Column(db.String(4000), nullable = False)

    def __init__(self, id_user, id_exercicio, resposta):
        self.id_user = id_user
        self.id_exercicio = id_exercicio
        self.resposta = resposta

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
        return {'id user': self.id_user, 'id exercicio':self.id_exercicio, 'resposta':self.resposta}