from fastapi import FastAPI, HTTPException
from database import bd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/login")
def login(email: str, senha: str):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * FROM Usuarios where email = %s and senha = %s"
        params = (email, senha)
        cursor.execute(sql, params)
        rows = cursor.fetchone()
        if rows:
            return {"id": rows["id"], "nome": rows["nome"]}
        else:
            raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")
    finally:
        cursor.close()

@app.post("/cadastro")
def cadastrar_usuarios(nome: str, email: str, senha: str):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Insert into Usuarios (nome,email,senha) values (%s,%s,%s)"
        params = (nome, email, senha)
        cursor.execute(sql, params) 
        bd.commit()
        return {"mensagem": "Cadastro realizado com sucesso"}
    except Exception as e:
        bd.rollback()
        raise HTTPException(status_code=400, detail="Erro: não foi possível cadastrar")
    finally:
        cursor.close()

@app.get("/tarefas")
def get_all_tarefas(idUsuario: int):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * from Tarefas where idUsuario = %s"
        cursor.execute(sql, (idUsuario,)) 
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao buscar tarefas")
    finally:
        cursor.close()
    
@app.get("/tarefas/{id}")
def get_tarefas(idUsuario: int, id: int):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * from Tarefas where idUsuario = %s and id = %s"
        params = (idUsuario, id)
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao buscar a tarefa")
    finally:
        cursor.close()
    
@app.post("/tarefas")
def cadastrar_tarefa(titulo: str, descricao: str, idUsuario: int):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Insert into Tarefas (titulo,descricao,status,idUsuario) values (%s,%s,%s,%s)"
        params = (titulo, descricao, "Pendente", idUsuario)
        cursor.execute(sql, params)
        bd.commit()
        return {"mensagem": "Tarefa criada com sucesso"}
    except Exception as e:
        bd.rollback()
        raise HTTPException(status_code=400, detail="Não foi possível criar a tarefa")
    finally:
        cursor.close()

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str, descricao: str, status: str):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Update Tarefas Set titulo = %s, descricao = %s, status = %s Where id = %s"
        params = (titulo, descricao, status, id)
        cursor.execute(sql, params)
        bd.commit()
        return {"mensagem": "Tarefa atualizada"}
    except Exception as e:
        bd.rollback()
        raise HTTPException(status_code=400, detail="Não foi possível atualizar")
    finally:
        cursor.close()

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Delete From Tarefas where id = %s"
        cursor.execute(sql, (id,)) 
        bd.commit()    
        return {"mensagem": "Tarefa deletada"}
    except Exception as e:
        bd.rollback()
        raise HTTPException(status_code=400, detail="Não foi possível deletar")
    finally:
        cursor.close()