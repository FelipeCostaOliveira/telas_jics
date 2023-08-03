from Equipe import *
import cadastro
import time

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
      print("\nProfessores cadastrados")
      cadastro.exibir_professores_cadastrados()
      print("\nAlunos cadastrados: ")
      cadastro.exibir_alunos_cadastrados()
      
      break
  print("\033[31mResposta inválida, digite 1 ou 2 \033[0;0m")
