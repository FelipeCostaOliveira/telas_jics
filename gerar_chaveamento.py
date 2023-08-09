import os
def equipes(caminho):
    for pasta, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo == "professores_cadastrados.txt":
                continue
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, "r", encoding="utf-8") as arq_txt:
                    conteudo = arq_txt.read()
                    linhas = conteudo.splitlines()
                    first_line = None
                    for linha in linhas:
                        if "Curso:" in linha:
                            palavras = linha.split()  # Dividir a linha em palavras
                            indice_curso = palavras.index("Curso:")
                            curso = palavras[indice_curso + 1]
                            turma = palavras[indice_curso + 3]
                            if first_line == None:
                                first_line = arq_txt.readline()
                    print(f"Equipe: {curso} {turma}")
                    print(conteudo)