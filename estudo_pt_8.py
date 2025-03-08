# n = int(input(" deposito inial :"))
# i = int(input(" taxa :"))
# tem = int(input(" quantidade de meses"))
# x = + 1 

# while x >= tem:
#     print("deposito por mes ")

# import time  
# for i in range(11):
#     print(i)
#     time.sleep(1)
# print("foguete foi lançado !!")

# m = int(input("deposito :"))
# i = int(input("valor da taxa :"))
# mes = int(input( "mes:" ))
# nv_valor =  int(input( "valor fixo mensal :" ))

# cal = m * i/100 *  mes 
# x = 0

# while x <=(mes-1):
#     x = x + 1 
#     print("{} mês = {} ".format(x, m * i/100 * x + m + (x * nv_valor)))

div = int(input("valor da dívida :"))
juros = int(input("juros mensal :"))
valor_pago_mensal = int(input("valor pago por mês :"))
x = 0

while  valor_pago_mensal <= div:
    x = x + 1 
    valor_pago_mensal = valor_pago_mensal + (valor_pago_mensal * juros/100)
    print("{} mês = R${:3.2f} ".format(x, valor_pago_mensal))
print("o valor da divida foi paga em {} meses".format(x))
    