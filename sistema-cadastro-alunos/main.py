alunos = []

def cadastrar_aluno():
   nome = input("Digite o nome do aluno: ")
   idade = int(input("Digite a idade do aluno: "))
   curso = input("Digite o curso do aluno: ")

   aluno = {
      "nome": nome,
      "idade": idade,
      "curso": curso
   }


   alunos.append(aluno)

   print("\n Aluno cadastrado com sucesso!")

def listar_alunos():
   print("\n--- ALUNOS CADASTRADOS ---")

   for aluno in alunos:
      print(f"Nome: {aluno['nome']}")
      print(f"Idade: {aluno['idade']}")
      print(f"Curso: {aluno['curso']}")
      print("--------------------------")


cadastrar_aluno()
listar_alunos()