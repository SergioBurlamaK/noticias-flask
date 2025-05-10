# 📰 Notícias com Flask e Web Scraping
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)

Este é um projeto web desenvolvido com **Flask** que realiza **web scraping** do portal de notícias [G1](https://g1.globo.com) e exibe as manchetes em uma interface simples e intuitiva. Além de visualizar as últimas manchetes, os usuários podem **filtrar as notícias** por palavras-chave usando a funcionalidade de busca.

🔗 **Acesse o projeto em produção:**  
👉 [https://noticias-flask.onrender.com](https://noticias-flask.onrender.com)

---

## 📚 Sumário

- [Demonstração](#-demonstração)
- [Como funciona](#-como-funciona)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Execução](#-instalação-e-execução)
- [Contribuindo](#-contribuindo)
- [Melhorias Futuras](#-melhorias-futuras)
- [Autor](#-autor)

---

## 📷 Demonstração

![Exemplo de uso](https://i.imgur.com/WeBThVx.gif)

---


## 🧠 Como funciona?

Este projeto realiza as seguintes etapas:

✅ Acessa o site do [G1](https://g1.globo.com) com uma requisição HTTP customizada.   
✅ Usa a biblioteca **BeautifulSoup** para fazer o parsing do HTML.   
✅ Seleciona os elementos que representam links de manchetes.   
✅ Constrói uma lista de dicionários com título e link de cada notícia.   
✅ Exibe essas informações em uma página HTML renderizada com Flask e Jinja2.   
✅ Permite buscar por palavras-chave que filtram as manchetes exibidas.  

---

## 🚀 Tecnologias Utilizadas

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" alt="flask logo"  />
</div>


## 📁 Estrutura do Projeto

```
noticias-flask/
├── app.py 
├── scraper.py
├── requirements.txt 
├── templates/
│   └── noticias.html

```

---

## 📦 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório:**
  ```bash
  git clone https://github.com/SergioBurlamaK/noticias-flask.git
  cd noticias-flask
  ```

2. **Crie um ambiente virtual e ative:**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```

3. **Instale as dependências:**
  ```bash
  pip install -r requirements.txt
  ```

4. **Execute o servidor:**
 ```bash
  python app.py
  ```

5. **Acesse no navegador:**
  ```bash
  http://localhost:5000
  ```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Você pode ajudar:
- Corrigindo bugs
- Melhorando o design das páginas
- Adicionando testes automatizados
- Expandindo para mais fontes de notícia

Para começar:
  ```
  git checkout -b feature/nome-da-feature
  git commit -m 'Adiciona nova feature'
  git push origin feature/nome-da-feature
  ```
Depois, abra um Pull Request 🚀

---

## 🔮 Melhorias Futuras

- **Filtro por categorias**: Permitir ao usuário selecionar temas como política, esportes, tecnologia etc.
- **Integração com outras fontes de notícias**: Expandir o scraping para sites como UOL ou CNN Brasil.
- **Atualização automática**: Agendar a raspagem de notícias em intervalos regulares com `APScheduler`.
- **API pública**: Criar uma API REST para disponibilizar as manchetes em formato JSON.
- **Melhorias no design responsivo**: Adaptar a interface para dispositivos móveis com um visual mais moderno.

---

## 👤 Autor

**Sergio Burlamaqui**

[![GitHub](https://img.shields.io/badge/GitHub-%40SergioBurlamaK-181717?style=for-the-badge&logo=github)](https://github.com/SergioBurlamaK)  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%40sergioburlamaqui-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sergioburlamaqui)

---

⭐️ Se você gostou do projeto, deixe uma estrela no GitHub e compartilhe!
