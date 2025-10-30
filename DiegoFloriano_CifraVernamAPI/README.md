# Cifra de Vernam API

**Integrantes do grupo:**
- Diego Floriano Costa

## 🚀 Como executar o projeto

1. Instale as dependências:
   bash
   pip install -r requirements.txt
   

2. Execute a API:
   bash
   uvicorn main:app --reload
   

3. Acesse no navegador:   http://127.0.0.1:8000/docs

## 🧠 Como usar

### Endpoint `/cifrar`
**POST**
```json
{
  "texto": "OLA MUNDO",
  "chave": "CHAVEGRANDE"
}
```

**Resposta:**
```json
{
  "mensagem_cifrada": "QUJDREVGR0hJSg=="
}
```

### Endpoint `/decifrar`
**POST**
```json
{
  "texto": "QUJDREVGR0hJSg==",
  "chave": "CHAVEGRANDE"
}
```

**Resposta:**
```json
{
  "mensagem_decifrada": "OLA MUNDO"
}
```


## 💡 Explicação
A cifra de Vernam usa a operação XOR entre cada caractere da mensagem e da chave.
A mesma função serve para cifrar e decifrar.
O resultado é codificado em base64 para facilitar o transporte de dados em JSON.
