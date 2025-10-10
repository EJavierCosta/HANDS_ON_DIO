# 🚀 Azure Function: Validação de CPF (Serverless)

Este repositório contém o código-fonte de um **Azure Function App** desenvolvido em **Python** para fornecer um endpoint de API Serverless para a validação de CPF.

A Function App é escalável (usando o Plano de Consumo) e implementa o algoritmo oficial de dígitos verificadores do CPF, sendo ideal para microserviços de validação.

---

## 🌟 Visão Geral do Projeto

| Característica | Detalhes |
| :--- | :--- |
| **Serviço Principal** | Azure Functions |
| **Linguagem (Runtime)** | Python (Modelo v2) |
| **Gatilho (Trigger)** | HTTP Trigger (API REST) |
| **Status Codes** | **`200 OK`** (CPF Válido) ou **`400 Bad Request`** (CPF Inválido/Entrada Inválida) |

---

## 🛠️ Tecnologias e Pré-requisitos

Para desenvolver e rodar este projeto, você precisará:

1.  **Python 3.x**
2.  **Azure Functions Core Tools** (`func`)
3.  **Visual Studio Code** (com a extensão Azure Functions)

---

## 📋 Como Testar a API (Endpoint)

A API espera uma requisição **POST** com o campo `cpf` no corpo JSON.

### 1. Endpoint de Produção (Azure)

O endpoint implantado utiliza o seguinte formato de rota:

[URL-BASE-DO-SEU-APP]/api/HttpValidaCpf?code=CHAVE_DE_FUNÇÃO

### 2. Exemplo de Requisição (JSON)

#### Requisição (Corpo JSON)
```json
{
    "cpf": "123.456.789-00"
}
```
#### Resposta de Erro (400 Bad Request)
```json
{
    "cpf": "12345678900",
    "mensagem": "CPF inválido."
}
```
#### Resposta de Sucesso (200 OK)
```json
{
    "cpf": "11144477701",
    "mensagem": "CPF válido."
}
```
