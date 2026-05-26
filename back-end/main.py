from fastapi import FastAPI
from database import bd
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/login")
def login(email,senha):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * FROM Usuarios where email = %s and senha = %s"
        params = (email,senha)
        cursor.execute(sql,params)
        rows= cursor.fetchone()
        return rows["id"]
    except:
        raise Exception("Usuario não encontrado")
    finally:
        cursor.close()

@app.post("/cadastro")
def cadastar_usuarios(nome,email,senha):
    cursor.execute(sql,params)
    try:
        sql = "Insert into Usuarios (nome,email,senha) values (%s,%s,%s)"
        params=(nome,email,senha)
        cursor = bd.cursor(dictionary=True)
        bd.commit()
        return "Cadastro com sucesso"
    except:
        raise Exception("Erro não foi possível cadastrar")
    finally:
        cursor.close()

@app.get("/tarefas")
def get_all_tareafas(idUsuario):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * from Tarefas where idUsuario = %s"
        cursor.execute(sql,idUsuario)
        rows = cursor.fetchall()
        return rows
    except:
        raise Exception("Erro")
    finally:
        cursor.close()
    
@app.get("/tarefas/{id}")
def get_tareafas(idUsuario,id):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Select * from Tarefas where idUsuario = %s and id = %s"
        params = (idUsuario,id)
        cursor.execute(sql,params)
        rows = cursor.fetchall()
        return rows
    except:
        raise Exception("Erro")
    finally:
        cursor.close()
    
@app.post("/tarefas")
def cadastrar_tarefa(titulo,descricao,idUsuario):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Insert into Tarefas (titulo,descricao,status,idUsuario) values (%s,%s,%s,%s)"
        params = (titulo,descricao,False,idUsuario)
        cursor.execute(sql,params)
        bd.commit()
        return "Tarefa criada"
    except:
        raise Exception("Não foi possível criar")
    finally:
        cursor.close()

@app.delete("/tarefas/{id}")
def deletar_tarefa(id):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Delete From Tarefas where id = %s"
        cursor.execute(sql,id)
        bd.commit()    
        return "Tarefa deletada"
    except:
        raise Exception("Não foi possível deletar")
    finally:
        cursor.close()

@app.put("/tarefas/{id}")
def atualizar_tarefa(titulo,descricao,status,id):
    cursor = bd.cursor(dictionary=True)
    try:
        sql = "Update Tarefas Set titulo = %s, descricao = %s, status = %s Where id = %s"
        params = (titulo,descricao,status,id)
        cursor.execute(sql,params)
        bd.commit()
        return "Tarefa atualizada"
    except:
        raise Exception("Não foi possível atualizar")
    finally:
        cursor.close()
