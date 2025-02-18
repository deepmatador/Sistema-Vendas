from fastapi import FastAPI, HTTPException
import uvicorn
from DataLogic import *
from ModelClass.Pyclass import *

# Inicializando o Servidor
app = FastAPI()

@app.post("/login")
async def RequestGetLogin(LoginForm: LoginData):
    try:

        print("Enviados para LOGIN")
        print(LoginForm.User, LoginForm.Password)

        response = await DataLoginUser(LoginForm.User, LoginForm.Password)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("Main-server:app", host="127.0.0.1", port=8000, reload=True)
