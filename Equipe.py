import os, sys
# --------------RENAN / DENY---------------------#
class Pessoa:
    def __init__(self, nome, matricula):
        self._nome = nome   # Convenção para indicar campo protegido
        self.__matricula = matricula  # Convenção para indicar campo privado
    def get_nome(self):
        return self._nome
        # Retorna o valor do campo "nome"

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        # Define um novo valor para o campo "nome"
    def get_matricula(self):
        return self.__matricula
        # Retorna o valor do campo "matricula"

class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso, turma):
        super().__init__(nome, matricula)
        self.curso = curso   # Campo público
        self.__turma = turma  # Convenção para indicar campo privado

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
        # Define um novo valor para o campo "matricula"

    def get_turma(self):
        return self.__turma
        # Retorna o valor do campo "turma"

    def set_turma(self, nova_turma):
        self.__turma = nova_turma
        # Define um novo valor para o campo "turma"

    
    def exibir_cadastro(self, sala, serie):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Curso: {sala}")
        print(f"Turma: {serie}")
        print()

    def cadastrar_aluno(self, serie, sala):
    #cria repositório
        if not os.path.isdir(sala):
            os.mkdir(sala)  

        caminho = os.path.join(sala, f"{serie}.txt")
    # Abrir o arquivo em modo de adição
        with open(caminho, "a", encoding="utf-8") as arquivo :
        # Escrever os dados do aluno no arquivo
            arquivo.write(f" Nome: {self.get_nome()}, Número Matrícula: {self.get_matricula()}, Curso: {serie} Turma: {sala}\n")
    

class professor(Pessoa):
    def __init__(self, nome, matricula, senha):
        super().__init__(nome, matricula)
        self.__senha = senha
        def get_senha(self):
          return self.__senha
        def set_senha(self, nova_senha):
          self.__senha = nova_senha
          
    def cad_professor(self, senha):       
      with open("professores_cadastrados.txt", "a", encoding="utf-8") as arquivo :
        # Escrever os dados do professor no arquivo
        arquivo.write(f" Nome: {self.get_nome()}, Número Matrícula: {self.get_matricula()}, Senha: {senha}\n")