# Data Collection Test

## Indice
- Técnologias utilizadas:
    - Bibliotecas: Pandas, requests, time, dateTime, json
    - Infra: Docker, Docker-compose
    - Data source: API Binance

## Técnologias
`Pandas: `Pandas é um pacote do python que fornece estruturas de dados rápidas, flexíveis e expressivas para tornar o trabalho com dados fácil e intuitivo.

`Requests: `Requests é uma biblioteca HTTP, projetada para interagir com a linguagem, facilitando nas consultas a URLs ou codificar dados POST.

`Time, DateTime: ` Módulo que fornece classes para trabalhar com datas e horas. Fornecendo várias funções para lidar com intervalos de tempos, ja que em python as datas e horas são objetos.

`Json: ` Biblioteca para manipulação de Json, Notação de objetos javaScript que é um formato leve usado para intercâmbio de dados.
`Docker: ` É uma plataforma de software que permitet a criação, o teste e a implantação de aplicações rapidamente.

`Docker-compose: ` É utilizado em composições de containers, facilitando a manipulação de volumes, networks, dependencias entre containers e etc.

`API Binance: ` Utilizado o link da documentação fornecida.

# Estratégia utilizada:
Criada uma função que recebe como parametro um inteiro que representa quantidade de dias, a partir disso utilizando os metodos da DateTime para recuperar o dia atual subtraimos a quantidade de dias que foi passada por parrametro para obter uma data inicio e fim, apos o calculo foi feita a conversão para timestamp para utilizar de parametro na requisição da API.

Outra função criada foi para alimentar o csv com as requisições, onde a cada iteração será carregado os dados da requisição em um dicionário então processado em um DataFrame para finalmente alimentar um arquivo csv(`file.csv`). O programa chega ao fim no momento em que  o range de dias for menor que 1. **Obs**: É utilizado um `try except` para verificar se a requisição retorna corretemente os dados, caso não retorne, imprime um warning contendo o range do timestamp referenciado a requisição.
Enquanto a `flag` continuar `True`, um laço `while` continuará iterando e executando uma requisição.  


# Utilização:
Para rodar localmente basta clonar este repositorio e rodar o comando `bash  init.sh`.

Para utilizar o projeto utilizando Docker execute o comando `dockeer-compose up --build`.