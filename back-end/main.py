from fastapi import FastAPI
from database import bd

app = FastAPI()

cursor = bd.cursor(dictionary=True)

@app.get("/login")
def login(email,senha):
    try:
        sql = "Select * FROM Usuarios where email = %s and senha = %s"
        params = (email,senha)
        cursor.execute(sql,params)
        rows= cursor.fetchone()
        return rows["id"]
    except:
        raise Exception("Usuario não encontrado")

@app.post("/cadastro")
def cadastar_usuarios(nome,email,senha):
    try:
        sql = "Insert into Usuarios (nome,email,senha) values (%s,%s,%s)"
        params=(nome,email,senha)
        cursor.execute(sql,params)
        bd.commit()
        return "Cadastro com sucesso"
    except:
        raise Exception("Erro não foi possível cadastrar")

@app.get("/tarefas")
def get_tareafas(idUsuario):
    try:
        sql = "Select * from Tarefas where idUsuario = %s"
        cursor.execute(sql,idUsuario)
        rows = cursor.fetchall()
        return rows
    except:
        raise Exception("Erro")
    
@app.get("/tarefas/{id}")
def get_tareafas(idUsuario,id):
    try:
        sql = "Select * from Tarefas where idUsuario = %s and id = %s"
        params = (idUsuario,id)
        cursor.execute(sql,params)
        rows = cursor.fetchall()
        return rows
    except:
        raise Exception("Erro")
    
@app.post("/tarefas/cadastrar")
def cadastrar_tarefa(titulo,descricao,idUsuario):
    try:
        sql = "Insert into Tarefas (titulo,descricao,status,idUsuario) values (%s,%s,%s,%s)"
        params = (titulo,descricao,False,idUsuario)
        cursor.execute(sql,params)
        bd.commit()
        return "Tarefa criada"
    except:
        raise Exception("Não foi possível criar")

@app.delete("/tarefas/deletar/{id}")
def deletar_tarefa(id):
    try:
        sql = "Delete From Tarefas where id = %s"
        cursor.execute(sql,id)
        bd.commit()
        return "Tarefa deletada"
    except:
        raise Exception("Não foi possível deletar")

@app.put("/tarefas/atualizar/{id}")
def atualizar_tarefa(titulo,descricao,status,id):
    try:
        sql = "Update Tarefas Set titulo = %s, descricao = %s, status = %s Where id = %s"
        params = (titulo,descricao,status,id)
        cursor.execute(sql,params)
        bd.commit()
        return "Tarefa atualizada"
    except:
        raise Exception("Não foi possível atualizar")
