import os
import random

def equipes(caminho, tam_chave):
    equipes_cadastradas = []
    for pasta, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo == "professores_cadastrados.txt":
                continue
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, "r", encoding="utf-8") as arq_txt:
                    conteudo = arq_txt.read()
                    linhas = conteudo.splitlines()
                    for linha in linhas:
                        if "Curso:" in linha:
                            palavras = linha.split()  # Dividir a linha em palavras
                            indice_curso = palavras.index("Curso:")
                            curso = palavras[indice_curso + 1]
                            turma = palavras[indice_curso + 3]
                            Equipe = f"{curso} {turma}"
                            equipes_cadastradas.append(Equipe)
    random.shuffle(equipes_cadastradas)
    num_equipes = len(equipes_cadastradas)
    
    with open("chaves.txt", "w", encoding="utf-8") as chvs:
        for i in range(0, num_equipes, tam_chave):
            chave = f"Chave {i // tam_chave + 1}: {' | '.join(equipes_cadastradas[i:i+tam_chave])}\n"
            chvs.write(chave)


