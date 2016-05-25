Organization patterns
===


### 1)

Sua aplicação pode ser estupidamente simples e caber tudo em um único arquivo,
como é o caso do "hello word".

    application.py


### 2)

Sua aplicação faz uso de templates e arquivos státicos.

    static/
    templates/
    application.py


### 3)

Sua aplicação começa a crescer e você separa o arquivo de configuração.

Além disso, temos o `requirements.txt`.

    static/
    templates/    
    application.py
    config.py
    requirements.txt

Deve ser semelhanta a...

    /yourapplication
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
        yourapplication.py
        config.py
        requirements.txt

