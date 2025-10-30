from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cifra de Vernam API")

class Mensagem(BaseModel):
    texto: str
    chave: str

def vernam_cipher(texto: str, chave: str) -> str:
    if len(chave) < len(texto):
        raise ValueError("A chave deve ter pelo menos o mesmo tamanho do texto.")
    resultado = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, chave))
    return resultado

@app.post("/cifrar")
def cifrar(msg: Mensagem):
    try:
        cifrado = vernam_cipher(msg.texto, msg.chave)
        import base64
        cifrado_b64 = base64.b64encode(cifrado.encode()).decode()
        return {"mensagem_cifrada": cifrado_b64}
    except Exception as e:
        return {"erro": str(e)}

@app.post("/decifrar")
def decifrar(msg: Mensagem):
    try:
        import base64
        texto_cifrado = base64.b64decode(msg.texto).decode()
        decifrado = vernam_cipher(texto_cifrado, msg.chave)
        return {"mensagem_decifrada": decifrado}
    except Exception as e:
        return {"erro": str(e)}
