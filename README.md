# Atividade-Microservice

Microserviço para cadastro e listagem de atividades vinculadas a professores.

---

## 🚀 Rotas disponíveis

### 📚 Atividades

- **Listar atividades:**  
  `GET http://127.0.0.1:5002/atividades`

- **Criar atividade:**  
  `POST http://127.0.0.1:5002/atividades`  
  Corpo da requisição (JSON):
  ```json
  {
    "id_professor": 1,
    "nome_atividade": "RPA",
    "nota": 5
  }
  ```

### 👤 Pessoas

- `GET http://127.0.0.1:5001/pessoas`

---

## ⚙️ Instalação e Configuração

1. Clone este repositório:
   ```sh
   git clone https://github.com/lirouana/Atividade-Microservice.git
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute o microserviço:
   ```sh
   python app.py
   ```

---

## 🗂️ Estrutura do Projeto

```
appAtividade/
├── app.py
├── config.py
├── controllers/
│   └── atividade_controller.py
├── models/
│   ├── bancoSQLite.py
│   └── atividade_model.py
├── clients/
│   └── pessoa_service_client.py
├── banco_de_dados.db
└── README.md
```

---

## 📝 Observações

- O serviço de atividades depende da API de professores disponível em:  
  `https://new-api-flask2.onrender.com/api/professores` (remoto) ou
  `http://127.0.0.1:5000/api/professores` => https://github.com/Alan-294/apis
- Para criar uma atividade, o `id_professor` deve existir na API de professores.
- Os dados devem ser enviados em formato JSON no corpo da requisição POST.

---
