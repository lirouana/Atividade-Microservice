from models.bancoSQLite import bd

class Atividades(bd):
    _tablename_ = 'Atividades'
    id = bd.Column(bd.Integer, primary_key=True)
    id_professor = bd.Column(bd.Integer, nullable=False)
    nome_atividade = bd.Column(bd.String(10), nullable=False)
    nota = bd.Column(bd.Decimal(10), nullable=False)
