# Usa uma imagem Python oficial
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta (ajustável se necessário)
EXPOSE 5002

# Executa o app
CMD ["python", "app.py"]
