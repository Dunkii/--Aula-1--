Nota1 = float(input("Insira a primeira nota: "))
Nota2 = float(input("Insira a segunda nota: "))
Media = (Nota1 + Nota2) / 2

if Media < 5:
    print("Aluno está reprovado.")
elif Media >= 5 and Media <= 6.9:
    print("Aluno está de recuperação.")
else:
    print ("Aluno está aprovado.")