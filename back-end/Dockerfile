#define a imagem, qual linguagem/framework
FROM python:3.14

WORKDIR /app

COPY requirements.txt .

#Comandos que serão rodados ao inicar o container
RUN pip install -r requirements.txt

COPY . .

#Mostra qual porta o container vai usar
EXPOSE 8000

#Comando executado quando sobe o container

#RUN roada uma vez e vira parte da iamgem CMD roda toda vez que subir o container
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]




