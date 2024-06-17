# Usar uma imagem base oficial do Python
FROM python:3.9

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /

# Copiar o arquivo de requisitos para o diretório de trabalho
COPY ./requirements.txt requirements.txt

# Instalar as dependências do Python (não há dependências neste exemplo)
RUN pip install -r requirements.txt

# Copiar o conteúdo do diretório atual para o diretório de trabalho no contêiner

COPY ./run.py ./run.py
# Comando para rodar a aplicação