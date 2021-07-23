# WEBSCRAPING/API RESULTADOS MEGA SENA


### Objetivo:

Esse projeto tem como objetivo construir uma API que faça jogos da mega sena, o usuario deverá escolher a quantidade de dezenas por jogo e sua API irá gerar aleatoriamente dezenas para o usuário. O usuário poderá consultar o resultado do ultimo jogo e comparar com suas dezenas para conferir quantos numeros acertou.
Para obter o ultimo resultado da megasena foi desenvolvido um webscrapping no Google, para obter dados do último resultado da mega sena.


### Instalação:

>git clone https://github.com/Nicolenewsoft/megasena.git

### Virtualenv:

>cd central_erros

>pip3 install virtualenv

>virtualenv venv -p python3

>source venv/bin/activate 

### Dependências:

>(venv) pip install -r requirements.txt

### Configurando:
>(venv) python manage.py migrate

>(venv) python manage.py createsuperuser

### Ativando o sistema:
>python manage.py runserver

### Coleção Postman:
[Documentação Postman](https://www.getpostman.com/collections/5687c7c04cdea059d09d)
