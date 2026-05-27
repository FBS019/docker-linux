import mysql.connector
import time
cont = 0

while cont < 5:
    try:    
        db = mysql.connector.connect(
            host="database-mysql",
            user="root",
            password="root",
            database="DockerLinux",
            port="3306"
        )
        print("conexão bem sucedida")
        break
    except:
        cont+=1
        print("Erro de conexão")
        print(f"Tentativa: {cont}/5")
        time.sleep(2)

if cont == 5:
    print("Erro não foi possível conectar ao banco")

