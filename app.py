from config import create_app
from controllers.atividade_controller import atividade_bp
from models.bancoSQLite import importar_professores_da_api
from models.bancoSQLite import inicializar_banco


app = create_app()
app.register_blueprint(atividade_bp)


inicializar_banco()
importar_professores_da_api()


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
