

    while oper2 == '-' or '+' or '*' or '/' or '+-' or '-+':
        date3 = int(input("ingrese número: "))
        oper3 = str(input("Ingrese '=' o '%': "))

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
        elif oper == '-' and oper2 == '+' and oper3 == '=':
            print(date1 - date2 + date3)
        elif oper == '-' and oper2 == '-' and oper3 == '=':
            print(date1 - date2 - date3)
        elif oper == '*' and oper2 == '=':
           print(date1 * date2)
        elif oper == '/' and oper2 == '=':
            print(date1 / date2)
        elif oper == '+-' or '-+' and oper2 == '+':
            print(date1 + date2 + date3)
            print(date1 - date2 + date3)