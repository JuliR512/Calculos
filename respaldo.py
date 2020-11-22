date1=1
date2=1
date3=1
oper=input()
oper2=input()
oper3=input()

while oper2 != '=' and oper3 != '=':
    date4 = int(input("ingrese número: "))
    oper4 = str(input("Ingrese '=': "))
    
    print(" ")
    print("Su resultado es: ")
    print(" ")

    #Suma
    #Suma y suma
    if oper == '+' and oper2 == '+' and oper3 == '+' and oper4 == '=':
        print(date1 + date2 + date3 + date4)
    elif oper == '+' and oper2 == '+' and oper3 == '-' and oper4 == '=':
        print(date1 + date2 + date3 - date4)
    elif oper == '+' and oper2 == '+' and oper3 == '*' and oper4 == '=':
        print(date1 + date2 + date3 * date4)
    elif oper == '+' and oper2 == '+' and oper3 == '/' and oper4 == '=':
        print(date1 + date2 + date3 / date4)
    #Suma y resta
    elif oper == '+' and oper2 == '-' and oper3 == '+' and oper4 == '=':
        print(date1 + date2 - date3 + date4)
    elif oper == '+' and oper2 == '-' and oper3 == '-' and oper4 == '=':
        print(date1 + date2 - date3 - date4)
    elif oper == '+' and oper2 == '-' and oper3 == '*' and oper4 == '=':
        print(date1 + date2 - date3 * date4)
    elif oper == '+' and oper2 == '-' and oper3 == '/' and oper4 == '=':
        print(date1 + date2 - date3 / date4)
    #Suma y multiplicacion
    elif oper == '+' and oper2 == '*' and oper3 == '+' and oper4 == '=':
        print(date1 + date2 * date3 + date4)
    elif oper == '+' and oper2 == '*' and oper3 == '-' and oper4 == '=':
        print(date1 + date2 * date3 - date4)
    elif oper == '+' and oper2 == '*' and oper3 == '*' and oper4 == '=':
        print(date1 + date2 * date3 * date4)
    elif oper == '+' and oper2 == '*' and oper3 == '/' and oper4 == '=':
        print(date1 + date2 * date3 / date4)
    #Suma y division
    elif oper == '+' and oper2 == '/' and oper3 == '+' and oper4 == '=':
        print(date1 + date2 / date3 + date4)
    elif oper == '+' and oper2 == '/' and oper3 == '-' and oper4 == '=':
        print(date1 + date2 / date3 + date4)
    elif oper == '+' and oper2 == '/' and oper3 == '*' and oper4 == '=':
        print(date1 + date2 / date3 * date4)
    elif oper == '+' and oper2 == '/' and oper3 == '/' and oper4 == '=':
        print(date1 + date2 / date3 / date4)
    #Resta
    #Resta y suma
    elif oper == '-' and oper2 == '+' and oper3 == '+' and oper4 == '=':
        print(date1 - date2 + date3 + date4)
    elif oper == '-' and oper2 == '+' and oper3 == '-' and oper4 == '=':
        print(date1 - date2 + date3 - date4)
    elif oper == '-' and oper2 == '+' and oper3 == '*' and oper4 == '=':
        print(date1 - date2 + date3 * date4)
    elif oper == '-' and oper2 == '+' and oper3 == '/' and oper4 == '=':
        print(date1 - date2 + date3 / date4)
    #Resta y resta
    elif oper == '-' and oper2 == '-' and oper3 == '+' and oper4 == '=':
        print(date1 - date2 - date3 + date4)
    elif oper == '-' and oper2 == '-' and oper3 == '-' and oper4 == '=':
        print(date1 - date2 - date3 - date4)
    elif oper == '-' and oper2 == '-' and oper3 == '*' and oper4 == '=':
        print(date1 - date2 - date3 * date4)
    elif oper == '-' and oper2 == '-' and oper3 == '/' and oper4 == '=':
        print(date1 - date2 - date3 / date4)
    #Resta y multiplicacion
    elif oper == '-' and oper2 == '*' and oper3 == '+' and oper4 == '=':
        print(date1 - date2 * date3 + date4)
    elif oper == '-' and oper2 == '*' and oper3 == '-' and oper4 == '=':
        print(date1 - date2 * date3 - date4)
    elif oper == '-' and oper2 == '*' and oper3 == '*' and oper4 == '=':
        print(date1 - date2 * date3 * date4)
    elif oper == '-' and oper2 == '*' and oper3 == '/' and oper4 == '=':
        print(date1 - date2 * date3 / date4)
    #Resta y division
    elif oper == '-' and oper2 == '/' and oper3 == '+' and oper4 == '=':
        print(date1 - date2 / date3 + date4)
    elif oper == '-' and oper2 == '/' and oper3 == '-' and oper4 == '=':
        print(date1 - date2 / date3 - date4)
    elif oper == '-' and oper2 == '/' and oper3 == '*' and oper4 == '=':
        print(date1 - date2 / date3 * date4)
    elif oper == '-' and oper2 == '/' and oper3 == '/' and oper4 == '=':
        print(date1 - date2 / date3 / date4)
    #Multiplicacion
    #Multiplicacion y suma
    elif oper == '*' and oper2 == '+' and oper3 == '+' and oper4 == '=':
        print(date1 * date2 + date3 + date4)
    elif oper == '*' and oper2 == '+' and oper3 == '-' and oper4 == '=':
        print(date1 * date2 + date3 - date4)
    elif oper == '*' and oper2 == '+' and oper3 == '*' and oper4 == '=':
        print(date1 * date2 + date3 * date4)
    elif oper == '*' and oper2 == '+' and oper3 == '/' and oper4 == '=':
        print(date1 * date2 + date3 / date4)
    #Multiplicacion y resta
    elif oper == '*' and oper2 == '-' and oper3 == '+' and oper4 == '=':
        print(date1 * date2 - date3 + date4)
    elif oper == '*' and oper2 == '-' and oper3 == '-' and oper4 == '=':
        print(date1 * date2 - date3 - date4)
    elif oper == '*' and oper2 == '-' and oper3 == '*' and oper4 == '=':
        print(date1 * date2 - date3 * date4)
    elif oper == '*' and oper2 == '-' and oper3 == '/' and oper4 == '=':
        print(date1 * date2 - date3 / date4)
    #Multiplicacion y multiplicacion
    elif oper == '*' and oper2 == '*' and oper3 == '+' and oper4 == '=':
        print(date1 * date2 * date3 + date4)
    elif oper == '*' and oper2 == '*' and oper3 == '-' and oper4 == '=':
        print(date1 * date2 * date3 - date4)
    elif oper == '*' and oper2 == '*' and oper3 == '*' and oper4 == '=':
        print(date1 * date2 * date3 * date4)
    elif oper == '*' and oper2 == '*' and oper3 == '/' and oper4 == '=':
        print(date1 * date2 * date3 / date4)
    #Multiplicacion y division
    elif oper == '*' and oper2 == '/' and oper3 == '+' and oper4 == '=':
        print(date1 * date2 / date3 + date4)
    elif oper == '*' and oper2 == '/' and oper3 == '-' and oper4 == '=':
        print(date1 * date2 / date3 - date4)
    elif oper == '*' and oper2 == '/' and oper3 == '*' and oper4 == '=':
        print(date1 * date2 / date3 * date4)
    elif oper == '*' and oper2 == '/' and oper3 == '/' and oper4 == '=':
        print(date1 * date2 / date3 / date4)
    #Division
    #Division y suma
    elif oper == '/' and oper2 == '+' and oper3 == '+' and oper4 == '=':
        print(date1 / date2 + date3 + date4)
    elif oper == '/' and oper2 == '+' and oper3 == '-' and oper4 == '=':
        print(date1 / date2 + date3 - date4)
    elif oper == '/' and oper2 == '+' and oper3 == '*' and oper4 == '=':
        print(date1 / date2 + date3 * date4)
    elif oper == '/' and oper2 == '+' and oper3 == '/' and oper4 == '=':
        print(date1 / date2 + date3 / date4)
    #Division y resta
    elif oper == '/' and oper2 == '-' and oper3 == '+' and oper4 == '=':
        print(date1 / date2 - date3 + date4)
    elif oper == '/' and oper2 == '-' and oper3 == '-' and oper4 == '=':
        print(date1 / date2 - date3 - date4)
    elif oper == '/' and oper2 == '-' and oper3 == '*' and oper4 == '=':
        print(date1 / date2 - date3 * date4)
    elif oper == '/' and oper2 == '-' and oper3 == '/' and oper4 == '=':
        print(date1 / date2 - date3 / date4)
    #Division y multiplicacion
    elif oper == '/' and oper2 == '*' and oper3 == '+' and oper4 == '=':
        print(date1 / date2 * date3 + date4)
    elif oper == '/' and oper2 == '*' and oper3 == '-' and oper4 == '=':
        print(date1 / date2 * date3 - date4)
    elif oper == '/' and oper2 == '*' and oper3 == '*' and oper4 == '=':
        print(date1 / date2 * date3 * date4)
    elif oper == '/' and oper2 == '*' and oper3 == '/' and oper4 == '=':
        print(date1 / date2 * date3 / date4)
    #Division y division
    elif oper == '/' and oper2 == '/' and oper3 == '+' and oper4 == '=':
        print(date1 / date2 / date3 + date4)
    elif oper == '/' and oper2 == '/' and oper3 == '-' and oper4 == '=':
        print(date1 / date2 / date3 - date4)
    elif oper == '/' and oper2 == '/' and oper3 == '*' and oper4 == '=':
        print(date1 / date2 / date3 * date4)
    elif oper == '/' and oper2 == '/' and oper3 == '/' and oper4 == '=':
        print(date1 / date2 / date3 / date4)
    break
