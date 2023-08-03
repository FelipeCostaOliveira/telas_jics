from Equipe import *
import os



def validar_matricula(matricula):
    return matricula.isdigit() and len(matricula) >= 10

def verificar_matricula_em_arquivos(caminho_diretorio, matricula):
    for pasta, _, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                    conteudo = arquivo_txt.read()
                    for linha in conteudo.splitlines():
                        if linha.strip() == "":
                            break
                        if matricula == linha.split(":")[2].replace(", Curso", "").strip():
                            return True
    return False



def exibir_alunos_cadastrados(caminho):
  # Abrir o arquivo em modo de leitura
  with open(caminho, "r", encoding="utf-8") as arquivo:
    # Ler as linhas do arquivo
    linhas = arquivo.readlines()
    # Imprimir os professores cadastrados
    for linha in linhas:
      # Remover a quebra de linha ao imprimir
      print(linha.rstrip())  



def exibir_professores_cadastrados():
  # 
  with open("professores_cadastrados.txt", "r", encoding="utf-8") as arquivo:
     
    linhas = arquivo.readlines()
     
    for linha in linhas:
       
      campos = linha.rstrip().split(",")
      
      nome = campos[0].split(":")[1].strip()
       
      matricula = campos[1].split(":")[1].strip()
      
      senha = campos[2].split(":")[1].strip()
      # Imprimir as informações formatadas na tela
      print(f"Nome: {nome}, Número de matrícula: {matricula}, Senha: {'*' * len(senha)}")

#--------------FELIPE------------------#


# Cadastrar um aluno
def cadastro():
 
  while True:
    nome = input("Digite o nome do discente: ").capitalize()
    matricula = input("Digite a matrícula do discente: ")

    while not validar_matricula(matricula):
        print("\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
        matricula = input("Digite a matrícula do discente:\n ")

    diretorio_raiz = os.getcwd()
    while True:
      if not verificar_matricula_em_arquivos(diretorio_raiz, matricula):
        break
      print("\033[31mJá existe um aluno cadastrado com essa matrícula.\033[0m")
      matricula = input("Digite a matrícula do discente:\n ")
        
    print(
      "\n \033[0mCursos disponíveis:\033[0m\n1 - \033[034mInformática\033[0m\n2 - \033[032mEletrotécnica\033[0m\n3 - \033[035mQuímica\033[0m\n4 - \033[031mEdificações\033[0m"
    )
    curso = input(
      "\nDigite o número correspondente ao curso do discente: ").capitalize()

    print(
      "\n\033[033mTurmas disponíveis:\n\033[0m1 - 1°A\n2 - 1°B\n3 - 2°Mat\n4 - 2°Vesp\n5 - 3°Mat\n6 - 3°Vesp"
    )
    turma = input(
      "Digite o número correspondente à turma do discente: ").capitalize()

    pessoa = Aluno(nome, matricula, curso, turma)
    print("\n\u001b[1m\033[032mCadastro realizado com sucesso!\033[0m\n")
   
    if curso == "1":
      sala = "Informática"
    elif curso == "2":
      sala = "Eletrotécnica"
    elif curso == "3":
      sala = "Química"
    elif curso == "4":
      sala = "Edificações"

    if turma == "1":
      serie = "1°A"
    elif turma == "2":
      serie = "1°B"
    elif turma == "3":
      serie = "2°Mat"
    elif turma == "4":
      serie = "2°Vesp"
    elif turma == "5":
      serie = "3°Mat"
    elif turma == "6":
      serie = "3°Vesp"

   
    pessoa.cadastrar_aluno(serie, sala)

    repetir = input("Deseja realizar um novo cadastro?\n1 - \033[032mSim\n\033[0m2 - \033[031mNão \033[0m")
    if repetir == '2':
      break
  print("\n\u001b[1m\033[032mCadastros Realizados na sua turma:\033[0m\n")
  caminho = os.path.join(sala, f"{serie}.txt")
  exibir_alunos_cadastrados(caminho)


def cadastro_professor():
  prof = []
  nome = input("Digite seu nome: ").capitalize()

  matricula_prof = input("Digite seu número de matrícula: ")
  while True:
    with open("alunos_cadastrados.txt", "r", encoding="utf-8") as arquivo:
      linhas = arquivo.readlines()
      for linha in linhas:
        if linha.strip() == "":
          break
        if matricula_prof == linha.split(":")[2].replace(", Senha", "").strip():
          print("\033[31mJá existe um aluno cadastrado com essa matrícula.\033[0m")
          matricula_prof = input("Digite seu número de matrícula: ")
          break

      else:
        # Se não houver matrícula repetida, sair do loop
        break

  senha = input("Digite sua senha: ")
  servidor = professor(nome, matricula_prof, senha)
  prof.append(servidor)
  servidor.cad_professor(senha)
