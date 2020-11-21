import math

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
    print("r =Raíz cuadrada")
    print(" ")
    print("INFORMACION IMPORTANTE:")
    print("los operadorees de '%' y '**' solo funcionan con 2 numeros a evaluar.")
    print("El operador 'r' solo funciona con un dato")

print(' ')

date1 = int(input("ingrese número: "))
oper = str(input("ingrese operador o =: "))

if oper == '=':
    print(" ")
    print("Su resultado es: ")
    print(" ")
    print(date1)

while date1<0 and oper=='r':
    print(" ")
    print("Error, no se puede sacar la raiz cuadrada de un numero negativo")
    print(" ")
    break

if oper =='r':
    date_4=math.sqrt(date1)
    print(" ")
    print("Su resultado es: ")
    print(" ")
    print(date_4)

#Aqui empieza un bucle

while oper != '=' and oper != 'r':
    date2 = int(input("ingrese número: "))
    oper2 = str(input("Ingrese operador, '=' o '%': "))

    date_Porcent = date2/100

    while oper2 != '=':
        date3 = int(input("ingrese número: "))
        oper3 = str(input("Ingrese '=' o '%': "))
        print(" ")
        print("Su resultado es: ")
        print(" ")

    #Suma
        if oper == '+' and oper2 == '+' and oper3 == '=':
            print(date1 + date2 + date3)
        elif oper == '+' and oper2 == '-' and oper3 == '=':
            print(date1 + date2 - date3)
        elif oper == '+' and oper2 == '*' and oper3 == '=':
            print(date1 + date2 * date3)
        elif oper == '+' and oper2 == '/' and oper3 == '=':
            print(date1 + date2 / date3)
        elif oper == '+' and oper2 == '+-' or '-+' and oper3 == '=':
            print(date1 + date2 + date3)
            print(date1 + date2 - date3)
    #Resta
        elif oper == '-' and oper2 == '+' and oper3 == '=':
            print(date1 - date2 + date3)
        elif oper == '-' and oper2 == '-' and oper3 == '=':
            print(date1 - date2 - date3)
        elif oper == '-' and oper2 == '*' and oper3 == '=':
            print(date1 - date2 * date3)
        elif oper == '-' and oper2 == '/' and oper3 == '=':
            print(date1 - date2 / date3)
        elif oper == '-' and oper2 == '-' and oper3 == '=':
            print(date1 - date2 + date3)
            print(date1 - date2 - date3)
    #Multiplicacion
        elif oper == '*' and oper2 == '+' and oper3 == '=':
           print(date1 * date2 + date3)
        elif oper == '*' and oper2 == '-' and oper3 == '=':
           print(date1 * date2 - date3)
        elif oper == '*' and oper2 == '*' and oper3 == '=':
           print(date1 * date2 * date3)
        elif oper == '*' and oper2 == '/' and oper3 == '=':
           print(date1 * date2 / date3)
        elif oper == '*' and oper2 == '+-' or '-+' and oper3 == '=':
           print(date1 * date2 + date3)
           print(date1 * date2 - date3)
    #Division
        elif oper == '/' and oper2 == '+' and oper3 == '=':
            print(date1 / date2 + date3)
        elif oper == '/' and oper2 == '-' and oper3 == '=':
            print(date1 / date2 - date3)
        elif oper == '/' and oper2 == '*' and oper3 == '=':
            print(date1 / date2 * date3)
        elif oper == '/' and oper2 == '/' and oper3 == '=':
            print(date1 / date2 / date3)
        elif oper == '/' and oper2 == '+-' or '-+' and oper3 == '=':
            print(date1 / date2 + date3)
            print(date1 / date2 - date3)
    #Suma y resta
        elif oper == '+-' or '-+' and oper2 == '+' and oper3 == '=':
            print(date1 + date2 + date3)
            print(date1 - date2 + date3)
        elif oper == '+-' or '-+' and oper2 == '-' and oper3 == '=':
            print(date1 + date2 - date3)
            print(date1 - date2 - date3)
        elif oper == '+-' or '-+' and oper2 == '*' and oper3 == '=':
            print(date1 + date2 * date3)
            print(date1 - date2 * date3)
        elif oper == '+-' or '-+' and oper2 == '/' and oper3 == '=':
            print(date1 + date2 / date3)
            print(date1 - date2 / date3)
        elif oper == '+-' or '-+' and oper2 == '+-' or '-+' and oper3 == '=':
            print(date1 + date2 + date3)
            print(date1 - date2 + date3)
            print(date1 + date2 - date3)
            print(date1 - date2 - date3)
        break;

    if oper == '+' and oper2 == '=':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 + date2)
    elif oper == '-' and oper2 == '=':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 - date2)
    elif oper == '*' and oper2 == '=':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 * date2)
    elif oper == '/' and oper2 == '=':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 / date2)
    elif oper == '+-' or '-+' and oper2 == '=' and oper != '**':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 + date2)
        print(date1 - date2)
    elif oper == '*' and oper2 == '%':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 * date_Porcent)
    elif oper == '**' and oper2 == '=':
        print(" ")
        print("Su resultado es: ")
        print(" ")
        print(date1 ** date2)
    break
