# desafio_tecnico
Este repositório tem como objetivo cumprir o desafio técnico proposto pela empresa como processo seletivo para vaga de Python.


Este projeto consiste em acessar uma matéria do Acorda Cidade e inserí-la em uma página web, utilizando Selenium para a automação e Django.

Tecnologias utilizadas:
- Django==3.1.2
- Selenium==3.141.0
- Python 3.8.2


Para rodar o projeto:

1. abrir o diretório do projeto no terminal do computador;
2. executar o comando ```python manage.py runserver```;
3. copiar o link que aparece (http://127.0.0.1:8000/) e colar no navegador.

OBS.: É necessário ter o arquivo chromedriver (executável que o Selenium WebDriver usa para controlar o Chrome) instalado no computador ou setado no PATH.

Lógica do projeto:

Copiei os IDs XPath da página do Acorda Cidade de cada parte do HTML da matéria e, utilizando o selenium, armazenei em uma varivável.
Após isso, inseri todos as variáveis com os IDs em um dicionário, com suas respectivas chaves, para ser lido pelo template do Django assim que a view for interpretada durante a chamada da URL.
Por fim, fiz a chamada das variáveis do dicionário no código HTML e estilizei utilizando CSS.