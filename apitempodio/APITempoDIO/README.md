# 🚀 API Simples de Previsão do Tempo (Mock)

Este repositório contém o código-fonte de uma **API Minimal em C# (.NET)**, seguindo a estrutura padrão de `WeatherForecast`, para simular dados de previsão do tempo.

O objetivo principal é fornecer um **endpoint HTTP** simples e robusto para testes e desenvolvimento, sem depender de serviços meteorológicos externos.

---

## 🌟 Visão Geral do Projeto e Arquitetura

| Característica | Detalhes |
| :--- | :--- |
| **Tecnologia (Backend)** | **C# / .NET 8** (Minimal API) |
| **Funcionalidade Central** | **Simulação/Mock** de 5 dias de previsão do tempo com valores aleatórios de temperatura e sumário. |
| **Documentação** | **Swagger/OpenAPI** embutido. |
| **Ambiente de Hospedagem** | **Azure Web App** (Containerizado) |
| **Registro de Imagem** | **Azure Container Registry (ACR)** |
| **CI/CD** | **Azure DevOps** (WebHook para atualização automática) |

---

## 🛠️ Detalhes Técnicos da API

A API expõe um único endpoint que retorna um array de objetos `WeatherForecast`.

### 1. Endpoint Único

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| **`GET`** | `/weatherforecast` | Retorna uma previsão simulada para os próximos 5 dias. |

### 2. Lógica de Simulação

O código C# utiliza `Random.Shared.Next` para gerar:
* **Temperatura em Celsius (`TemperatureC`)**: Aleatória entre -20°C e 55°C.
* **Sumário (`Summary`)**: Um texto aleatório (ex: "Freezing", "Hot", "Mild") da lista pré-definida.
* **Conversões**: As propriedades `TemperatureF` (Fahrenheit) e `TemperatureK` (Kelvin) são calculadas automaticamente.

### 3. Exemplo de Resposta (200 OK)

```json
[
  {
    "date": "2025-10-15",
    "temperatureC": 18,
    "summary": "Cool",
    "temperatureF": 64,
    "temperatureK": 291
  },
  // ... mais 4 dias
]
