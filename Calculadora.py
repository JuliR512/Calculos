print(' ')
print("CALCULADORA DE OPERACIONES BASICAS")
print(" ")
help = str(input('ingrese "help" si requiere ayuda: '))

#Icono de ayuda

if help == 'help':
    print(' ')
    print("Comandos:")
    print(' ')
    print("+ = suma")
    print("- = resta")
    print("+- o -+ = suma y resta")
    print("* = multiplicacion")
    print("/ = division")
    print("primero: *, y despues: % = porcentaje")
    print("** = exponentes")

print(' ')

date1 = int(input("ingrese número: "))
oper = str(input("ingrese operador o =: "))

if oper == '=':
    print(date1)

#Aqui empieza un bucle

while oper == '-' or '+' or '*' or '/' or '+-' or '-+':
    date2 = int(input("ingrese número: "))
    oper2 = str(input("Ingrese '=' o '%': "))

    date_Porcent = date2/100

    if oper == '+' and oper2 == '=':
        print(date1 + date2)
    elif oper == '-' and oper2 == '=':
        print(date1 - date2)
    elif oper == '*' and oper2 == '=':
        print(date1 * date2)
    elif oper == '/' and oper2 == '=':
        print(date1 / date2)
    elif oper == '+-' or '-+' and oper2 == '=' and oper != '**':
        print(date1 + date2)
        print(date1 - date2)
    elif oper == '*' and oper2 == '%':
        print(date1 * date_Porcent)
    elif oper == '**' and oper2 == '=':
        print(date1 ** date2)
    break