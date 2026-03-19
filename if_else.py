#1

print(1, True and True)
print(2, False and True)                    
print(3, 1 == 1 and 2 == 1)                  
print(4, "test" == "test")                   
print(5, 1 == 1 or 2 != 1)             
print(6, True and 1 == 1)                    
print(7, False and 0 != 0)                  
print(8, True or 1 == 1)                    
print(9, "test" == "testing")                
print(10, 1 != 0 and 2 == 1)                 
print(11, "test" != "testing")              
print(12, "test" == 1)                       
print(13, not (True and False))              
print(14, not (1 == 1 and 0 != 1))           
print(15, not (10 == 1 or 1000 == 1000))     
print(16, not (1 != 10 or 3 == 4))           
print(17, not ("testing" == "testing" and "Zed" == "Cool Guy"))  
print(18, 1 == 1 and (not ("testing" == 1 or 1 == 0)))    
print(19, "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))      
print(20, 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))




#2

num = int(input("Digite um número: "))

if num >= 0:
    print("Número positivo")
else:
    print("Número negativo")
    



#3

valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas: "))
salario = float(input("Salário: "))

valor_parcela = valor / parcelas

if valor_parcela <= salario * 0.3:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")
    
    
    
    
#4
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")
    


#5

valor_hora = float(input("Valor da hora: "))
horas = float(input("Horas trabalhadas: "))
inss = float(input("Percentual INSS (%): "))

salario_bruto = valor_hora * horas
desconto = salario_bruto * (inss / 100)
salario_liquido = salario_bruto - desconto

print("Salário bruto:", salario_bruto)
print("Salário líquido:", salario_liquido)



#6
a = float(input("Digite A: "))
b = float(input("Digite B: "))

if a > b:
    print("Maior:", a)
else:
    print("Maior:", b)



#7

p1 = float(input("Nota 1: "))
p2 = float(input("Nota 2: "))
p3 = float(input("Nota 3: "))

media = (p1*2 + p2*3 + p3*5) / 10

print("Média final:", media)




#16

nome = input("Nome do candidato: ")

port = float(input("Nota Português: "))
mat = float(input("Nota Matemática: "))
geral = float(input("Nota Conhecimentos Gerais: "))

media = (port + mat + geral) / 3

print("\nNome:", nome)
print("Notas:", port, mat, geral)
print("Média:", media)

if media > 7 and port >= 5 and mat >= 5 and geral >= 5:
    print("Aprovado")
else:
    print("Reprovado")

