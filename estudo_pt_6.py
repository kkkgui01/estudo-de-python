valor = float(input("qual o valor da casa? :"))
salario = float(input("qual seu salario ? :"))
anos = int(input("quantos anos voce deseja pagar essa casa ? :"))
prestacao_mensal = valor /( anos * 12)

if prestacao_mensal > salario * 0.30 :
    print("nao podemos fazer essa ação")
else:
    print(" o emprestimo foi aceito ") 
