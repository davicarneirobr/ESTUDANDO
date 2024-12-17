# Modulos em python
# modulos sao arquivos em .py contendo
    # definicoes 
    # comandos (statements)

# um modulo pode ser importado por outro utilizando o comando import

# o nome do modulo (nome do arquivo sem a extensao .py) fica disponivel na variavel __name__ 

print (__name__)

if __name__ == "__main__":
    # ai posso fazer comandos de inicializacao
    import sys