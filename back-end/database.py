import mysql.connector

cont = 0

while cont < 5:
    try:    
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="DockerLinux"
        )
        print("conexão bem sucedida")
        break
    except:
        cont+=1
        print("Erro de conexão")
        print(f"Tentativa: {cont}/5")

if cont == 5:
    print("Erro não foi possível conectar ao banco")

