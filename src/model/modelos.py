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

