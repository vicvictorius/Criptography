# 🔐 Criptografia e Descriptografia de Arquivos com Python
## 📌 Descrição / Description

**🇧🇷 Português:**

Este projeto contém dois scripts Python para criptografar e descriptografar arquivos em diretórios específicos do usuário no Windows usando a biblioteca cryptography.

- `toilet.py` → Criptografa os arquivos e salva a chave de criptografia (`chave.key`).

- `skibidi.py` → Descriptografa os arquivos utilizando a chave armazenada.

**⚠️ ATENÇÃO:**

 O uso inadequado destes scripts pode resultar na perda permanente de arquivos. Guarde a chave de criptografia (`chave.key`) com segurança, pois sem ela a recuperação dos arquivos não será possível.

#

**🇺🇸 English:**

This project contains two Python scripts to **encrypt and decrypt** files in specific user directories on Windows using the **cryptography** library.

- `toilet.py` → Encrypts files and saves the encryption key (`chave.key`).

- `skibidi.py` → Decrypts files using the stored key.

**⚠️ WARNING:**

Improper use of these scripts may result **in permanent file loss. Keep the encryption key** (`chave.key`) **safe**, as file recovery will not be possible without it.

# 
# 🛠️ Como funciona / How it works

🔒 `toilet.py` **(Criptografar arquivos / Encrypt files)**
 
   1. **Gera uma chave de criptografia** e a salva no arquivo `chave.key`.

   2. **Busca arquivos nos diretórios do usuário** (`Documents`, `Pictures`, `Videos`, `Downloads`).

   3. **Criptografa os arquivos encontrados e substitui os originais pelos arquivos criptografados.**

   4. Ignora arquivos protegidos, como `chave.key`, `desktop.ini` e os próprios scripts.

🔓 `skibidi.py` **(Descriptografar arquivos / Decrypt files)**
   1. **Lê a chave de criptografia do arquivo** `chave.key`.

   2. **Percorre os mesmos diretórios** em busca dos arquivos criptografados.

   3. **Descriptografa os arquivos e restaura o conteúdo original.**

   4. Se `chave.key` estiver ausente, a descriptografia não será **possível.**

   #

   # 🚀 Como executar / How to run
 **1️⃣ Instalar dependências / Install dependencies**

 🇧🇷 Certifique-se de ter o Python instalado e instale a biblioteca necessária:
🇺🇸 Make sure you have Python installed and install the required library:

``` pip install cryptography ```

 **2️⃣ Executar o script de criptografia / Run the encryption script**
 
 ``` pip toilet.py ```

 **🛑 IMPORTANTE:** O script **irá criptografar seus arquivos!** Certifique-se de ter um backup.

**3️⃣ Executar o script de descriptografia / Run the decryption script**

Se precisar recuperar os arquivos, execute:

``` pip skibidi.py```
# 
# 🔑 Recuperação de arquivos / File Recovery

**✅ 🇧🇷 Português:**

- Se `chave.key` for perdida, **não será possível recuperar os arquivos.**

- Para descriptografar, basta rodar `skibidi.py` com a chave salva.

**✅ 🇺🇸 English:**

- If `chave.key` is lost, **files cannot be recovered.**

- To decrypt, simply run `skibidi.py` with the saved key.

#
# ⚠️ Aviso Legal / Legal Notice

**🇧🇷 Português:**
Este código deve ser usado **apenas para fins educacionais ou pessoais.** O uso indevido para criptografar arquivos sem autorização pode ser **ilegal** e sujeito a penalidades.

**🇺🇸 English:**
This code should be used **only for educational or personal purposes.** Unauthorized encryption of files may be **illegal** and subject to penalties.






  
