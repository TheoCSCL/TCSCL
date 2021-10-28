numero1 = int(input("Digite o numero!")) 
numero2 = int(input("Digite o numero!")) 

soma = numero1 + numero2 
sub = numero1 - numero2
mult = numero1 * numero2

if numero2 != 0:
    div = numero1 / numero2 

print("A soma do",numero1,"mais o",numero2,"deu",soma)
print("A sub do",numero1,"menos o",numero2,"deu",sub)
print("A mult do",numero1,"vezes o",numero2,"deu",mult) 
print("A div do",numero1,"dividido por",numero2,"deu",div)