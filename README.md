# Central de Erros
## Api Rest | Projeto Prático AceleraDev | Codenation

![Api](https://user-images.githubusercontent.com/35440249/87815852-ba745300-c83c-11ea-830d-97980b45b213.PNG)

![admin](https://user-images.githubusercontent.com/35440249/87876879-4effc200-c9b1-11ea-9e97-6e9717531c60.PNG)


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
