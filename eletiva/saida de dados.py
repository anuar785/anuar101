idade: int
salario: float
nome: str 
sexo: str

idade = 20
salario = 6340.60
nome = "Carlos Fereira"
sexo = "M"

print(F"0 funcionário {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

print("O funcionario {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))