from Equipe import *
import cadastro
import time
from registro import *
from gerar_chaveamento import equipes

'''frase = "\033[3;0;97m\n        Avaliação Prática -  Programação Orientada a Objetos(POO)\n                   2º ANO - Informática - Matutino\n\n                            Grupo Valhalla\n\nDocente:\n -> Camila Serrão\n\nDiscentes:\n -> Deny Willian de Lima Martins\n -> Felipe Costa de Oliveira \n -> Renan Neponuceno Barroso\n -> Stefano Gabriel Mendonça de Oliveira\n"


for i in frase:
  time.sleep(0.000001)
  print(i,end='', flush=True)
print()'''
diretório_raiz = os.getcwd()
print(f'este é o diretório raiz{diretório_raiz}')
print("Quem deseja acessar?")
while True:
  quem = int(input("1 - Aluno que irá cadastrar\n2 - Professores\n"))

  if quem == 1:
      cadastro.cadastro()
      
      break
  elif quem == 2:
      cadastro.cadastro_professor()
      print("\nAlunos cadastrados: ")
      
      caminho_diretorio = os.getcwd()
      for pasta, _, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo == "professores_cadastrados.txt":
              continue
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                    conteudo = arquivo_txt.read()
                    print(conteudo)
      break
    
  elif quem == 3:
    caminho_raiz = os.getcwd()
    equipes(caminho_raiz)
    break
  print("\033[31mResposta inválida, digite 1 ou 2 \033[0;0m")
