# Sistema de Mensageria com Logs Centralizados

###### AUTOR: ALYSSON C. C. CORDEIRO - ENGENHEIRO DA COMPUTAÇÃO (INTELI)

## Objetivo

O objetivo deste projeto é implementar um sistema de mensageria com logs centralizados. O sistema é composto por um gateway, um serviço de eventos e um serviço de logs centralizado. O gateway roteia as requisições para o serviço de eventos, enquanto ambos os serviços registram logs localmente e enviam logs para o serviço centralizado.

## Estrutura do Projeto

```python
ponderada4_m10/
├── mensagem/
│ ├── gateway/
│ │ ├── gateway.py
│ │ ├── Dockerfile
│ │ └── requirements.txt
│ ├── eventos/
│ │ ├── eventos.py
│ │ ├── Dockerfile
│ │ └── requirements.txt
│ ├── logs/
│ │ ├── logs.py
│ │ ├── Dockerfile
│ │ └── requirements.txt
├── logs/
│ ├── gateway.log
│ ├── eventos.log
│ └── logs.log
├── docker-compose.yml
└── README.md
```


## Descrição dos Componentes

### Gateway

- **Arquivo:** `gateway/gateway.py`
- **Função:** Roteia as requisições para o serviço de eventos.
- **Logs:** Registra logs localmente em `gateway.log` e envia logs para o serviço centralizado de logs.

### Serviço de Eventos

- **Arquivo:** `eventos/eventos.py`
- **Função:** Gerencia operações CRUD para eventos.
- **Logs:** Registra logs localmente em `eventos.log` e envia logs para o serviço centralizado de logs.

### Serviço de Logs

- **Arquivo:** `logs/logs.py`
- **Função:** Recebe e armazena logs enviados pelos serviços de gateway e eventos.

## Endpoints

### Gateway

- **POST /eventos**
  - Cria um novo evento.
  - **Body (JSON):**
    ```json
    {
      "id": 1,
      "nome": "Evento de Teste",
      "data": "2024-06-18"
    }
    ```

- **GET /eventos**
  - Retorna todos os eventos.

- **PUT /eventos**
  - Atualiza um evento existente.
  - **Body (JSON):**
    ```json
    {
      "id": 1,
      "nome": "Evento Atualizado",
      "data": "2024-06-19"
    }
    ```

- **DELETE /eventos**
  - Deleta um evento.
  - **Body (JSON):**
    ```json
    {
      "id": 1
    }
    ```

### Serviço de Logs

- **POST /logs**
  - Adiciona um novo log.
  - **Body (JSON):**
    ```json
    {
      "log": "Mensagem de log"
    }
    ```

- **GET /logs**
  - Retorna todos os logs armazenados.

## Como Executar o Projeto

1. **Clonar o Repositório:**
   ```sh
   git clone https://github.com/alyssoncastro/ponderada4_m10.git
   cd ponderada4_m10
   ```

2. **Subir os Containers com Docker Compose:**

    ```sh
    docker-compose up --build
    ```
3. **Teste:**

 Ultilizei a ferramenta do Thunder Client

### Demostração:

1. Gateway Logs (gateway.log)

    
```sh
2024-06-19 12:00:33,684 GET /eventos 200
2024-06-19 12:00:48,410 POST /eventos 201
2024-06-19 12:01:59,251 PUT /eventos 200
2024-06-19 12:02:15,244 DELETE /eventos 200
2024-06-19 12:02:17,082 DELETE /eventos 404
```

2. Eventos Logs (eventos.log)

```sh
2024-06-19 12:00:33,683 172.22.0.4 - - [19/Jun/2024 12:00:33] "GET /eventos HTTP/1.1" 200 -
2024-06-19 12:00:48,402 POST /eventos {'id': 1, 'nome': 'Evento de Teste', 'data': '2024-06-18'}
2024-06-19 12:01:59,245 PUT /eventos {'id': 1, 'nome': 'Evento Atualizado', 'data': '2024-06-19'}
2024-06-19 12:02:15,239 DELETE /eventos 1
2024-06-19 12:02:17,080 172.22.0.4 - - [19/Jun/2024 12:02:17] "DELETE /eventos HTTP/1.1" 404 -

```

## Vídeo:

https://drive.google.com/file/d/1O78RHnS9AQjcxHDdV_AmWWSCur52IcNq/view?usp=sharing