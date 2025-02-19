from fastapi import FastAPI, HTTPException
import uvicorn
from Datalogic import *
from classmodel import LoginData


# Inicializando o Servidor
app = FastAPI()

@app.post("/login")
async def RequestGetLogin(LoginForm: LoginData):
    try:

        print("Enviados para LOGIN")
        print(LoginForm.User, LoginForm.Password)

        #Se optar por banco de dados real, Baixe mysql, configure-o e importe o banco pbstock.sql para ele
        #E mude a função para Dataloginuser
        response = await DataloginSemBanco(LoginForm.User, LoginForm.Password)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("Mainserver:app", host="127.0.0.1", port=8000, reload=True)

