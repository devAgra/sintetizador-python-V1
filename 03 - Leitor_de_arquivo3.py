# Importando um arquivo .txt e fazendo a leiitura deste arquivo

arquivo = open("frase.txt", "r")  # arquivo encotra-se no mesmo diretório
conteudo = arquivo.read()          # Lendo o arquivo
print(conteudo)                    # Confirmando se o arquivo foi lido
arquivo.close()                    # fechando o arquivo 

