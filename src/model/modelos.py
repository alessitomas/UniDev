from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import *
from model.sql_alchemy_para_db import db
import sqlalchemy
from flask_login import UserMixin





class CursoModel(db.Model):
    _tablename__ = "curso_model"

    id_curso = db.Column(db.Integer, primary_key=True )
    nome_curso = db.Column(db.String(80), nullable = False)
    linguagem = db.Column(db.String(20), nullable = False)
    ##exercicios = db.relationship('ExerciciosModel', secondary="tbl_exercicios", backref='tabela_exercicios') 

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

class UsuarioModel(db.Model, UserMixin):
    _tablename__ = "usuario_model"

    id_usuario = db.Column(db.Integer, primary_key=True )
    nome_usuario = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    ##exercicios = db.relationship('ExerciciosModel', secondary="tbl_exercicios", backref='tabela_exercicios') 

    def __init__(self, id_usuario, nome_usuario, email):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email = email

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

matricula_curso = db.Table('tbl_matricula_curso',
                    db.Column('curso_id', db.Integer, db.ForeignKey('curso_model.id_curso')),
                    db.Column('matricula_id', db.Integer, db.ForeignKey('matricula_model.id_matricula'))
                    )

matricula_usuario = db.Table('tbl_matricula_usuario',
                    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario_model.id_usuario')),
                    db.Column('matricula_id', db.Integer, db.ForeignKey('matricula_model.id_matricula'))
                    )

class MatriculaModel(db.Model):
    _tablename__ = "matricula_model"

    EM_ABERTO = 0
    CONCLUIDO = 1

    usuario = db.relationship('UsuarioModel', secondary="tbl_matricula_usuario", backref='relacao_matricula_usuario')
    curso = db.relationship('CursoModel', secondary="tbl_matricula_curso", backref='relacao_matricula_curso')
    inicio = db.Column(db.DateTime, nullable = False)
    status= db.Column(db.Boolean, default=0)
    fim= db.Column(db.DateTime)
    id_matricula = db.Column(db.Integer, primary_key = True)


    def __init__(self, inicio, status, fim, id_matricula):
        self.inicio = inicio
        self.status = status
        self.fim = fim
        self.id_matricula = id_matricula

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
        return {'id user': self.id_user, 'id curso':self.id_curso, 'inicio':self.inicio, 'status':self.status, 'fim':self.fim, 'matricula': self.id_matricula}

exercicios = db.Table('tbl_exercicios',
                    db.Column('curso_id', db.Integer, db.ForeignKey('curso_model.id_curso')),
                    db.Column('exercicio_id', db.Integer, db.ForeignKey('exercicios_model.id_exercicio'))
                    )

class ExerciciosModel(db.Model):
    _tablename__ = "exercicios_model"

    id_exercicio = db.Column(db.Integer, primary_key=True, nullable = False)
    curso = db.relationship('CursoModel', secondary="tbl_exercicios", backref='relacao_curso_exercicio')
    tela = db.Column(db.Integer)
    pytest = db.Column(db.String(4000))
    titulo = db.Column(db.String(80))
    enunciado = db.Column(db.String(4000), nullable = False)
    gabarito = db.Column(db.String(4000), nullable = False)

    def __init__(self, id_exercicio,tela, enunciado, gabarito, pytest, titulo):
        self.id_exercicio = id_exercicio
        self.tela = tela
        self.pytest = pytest
        self.titulo = titulo
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
        return {'id exercicio': self.id_exercicio, 'tela':self.tela, 'enunciado':self.enunciado, 'gabarito':self.gabarito, 'titulo': self.titulo}


resposta_usuario = db.Table('tbl_resposta_usuario',
                    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario_model.id_usuario')),
                    db.Column('resposta_id', db.Integer, db.ForeignKey('respostas_model.id_resposta'))
                    )

resposta_exercicio = db.Table('tbl_resposta_exercicio',
                    db.Column('exercicio_id', db.Integer, db.ForeignKey('exercicios_model.id_exercicio')),
                    db.Column('resposta_id', db.Integer, db.ForeignKey('respostas_model.id_resposta'))
                    )

class RespostasModel(db.Model):
    _tablename__ = "respostas_model"

    usuario = db.relationship('UsuarioModel', secondary="tbl_resposta_usuario", backref='relacao_usuario_resposta')
    exercicio = db.relationship('ExerciciosModel', secondary="tbl_resposta_exercicio", backref='relacao_exercicio_resposta')
    resposta = db.Column(db.String(4000), nullable = False)
    id_resposta = db.Column(db.Integer, primary_key = True)

    def __init__(self, resposta, id_resposta):
        self.resposta = resposta
        self.id_resposta = id_resposta

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
        return {'id exercicio':self.id_resposta, 'resposta':self.resposta}