FROM node:20

WORKDIR /app

# copiar os arquivos das dependecias
COPY package.json package-lock.json* ./

# Instalar as dependencias
RUN npm install

# copiar o restante
COPY . .

#Porta que vai estar exposta
EXPOSE 5173

# comando para rodar o vite
CMD ["npm", "run", "dev", "--", "--host"]
