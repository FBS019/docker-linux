import mysql.connector
import time
cont = 0

bd = None 

while cont < 10:
    try:    
        bd = mysql.connector.connect(
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
        time.sleep(3)

if cont == 10 or bd is None:
    print("Erro não foi possível conectar ao banco")

