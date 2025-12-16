# 🚀 GitHub User Viewer com Streamlit

Aplicação simples desenvolvida em **Streamlit** que realiza uma requisição à **API pública do GitHub** para buscar e exibir informações de um usuário a partir do *username* digitado.

DEPLOY: https://app-api-users-git-h-ub.streamlit.app/

---

## 📌 Funcionalidades

* Campo de texto para digitar o nome de usuário do GitHub
* Requisição à API pública do GitHub (`https://api.github.com/users/{username}`)
* Exibição de informações básicas do usuário
* Tratamento de erros para usuários inexistentes ou problemas na requisição

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* **Streamlit**
* **Requests**
* **API do GitHub**

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/raizera/Streamlit-API.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

No terminal, execute:

```bash
streamlit run app.py
```

Após isso, o navegador será aberto automaticamente com a aplicação.

---

## 🧪 Exemplo de Uso

1. Digite um nome de usuário válido do GitHub (ex: `torvalds`)
2. A aplicação fará a requisição à API
3. Os dados do usuário serão exibidos na tela

---

## 📄 Estrutura do Projeto

```text
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Observações

* A API do GitHub possui **limite de requisições** para usuários não autenticados.
* Para projetos maiores, recomenda-se o uso de **token de autenticação**.

---

## 📜 Licença

Este projeto é livre para fins de estudo e aprendizado.

---

👨‍💻 Desenvolvido com Python e Streamlit
