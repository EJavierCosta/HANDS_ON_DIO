import azure.functions as func
import json
import logging
import re # Importar a biblioteca de expressões regulares para limpeza

app = func.FunctionApp()

# --- FUNÇÃO AUXILIAR DE VALIDAÇÃO DO CPF ---
def validar_cpf(cpf):
    """
    Função para validar o CPF através dos dígitos verificadores.
    """
    # 1. Limpa e Verifica o Tamanho
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11:
        return False

    # 2. Verifica se todos os dígitos são iguais (e-book: 111.111.111-11, que é inválido)
    if cpf == cpf[0] * 11:
        return False

    # 3. Cálculo do 1º Dígito Verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    if int(cpf[9]) != digito1:
        return False

    # 4. Cálculo do 2º Dígito Verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if int(cpf[10]) != digito2:
        return False

    return True

# --- FUNÇÃO PRINCIPAL DA AZURE FUNCTION (HTTP Trigger) ---
@app.route(route="HttpValidaCpf", auth_level=func.AuthLevel.FUNCTION)
def HttpValidaCpf(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function (HttpValidaCpf) processing a request.')

    try:
        # Tenta obter o CPF do corpo da requisição JSON (POST)
        req_body = req.get_json()
        cpf_input = req_body.get('cpf')
    except ValueError:
        # Se não for JSON, tenta obter da Query String (GET)
        cpf_input = req.params.get('cpf')

    # 1. Verifica se o CPF foi fornecido
    if not cpf_input:
        return func.HttpResponse(
             json.dumps({"status": "erro", "mensagem": "Por favor, forneça o CPF no corpo da requisição JSON (chave 'cpf') ou na query string."}),
             status_code=400,
             mimetype="application/json"
        )

    # 2. Valida o CPF
    if validar_cpf(cpf_input):
        resultado = {
            "status": "sucesso",
            "cpf": cpf_input,
            "valido": True,
            "mensagem": "CPF válido."
        }
        status_code = 200
    else:
        resultado = {
            "status": "erro",
            "cpf": cpf_input,
            "valido": False,
            "mensagem": "CPF inválido."
        }
        status_code = 400

    # 3. Retorna a resposta JSON
    return func.HttpResponse(
        json.dumps(resultado),
        status_code=status_code,
        mimetype="application/json"
    )