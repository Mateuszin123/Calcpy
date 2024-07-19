conta = input("Calcular: ")
conta = list(conta.split())

value1 = 0
value2 = 0
operador = ''
for i in conta:
    if i not in ['/', '*', '+', '-']:
        if value1 == 0 and operador == '': value1 = float(i)
        if operador != '':
            value2 = float(i)
            if operador == '+':
                print(value1 + value2)
            if operador == '-':
                print(value1 - value2)
            if operador == '*':
                print(value1 * value2)
            if operador == '/':
                print(value1 / value2)
    else: operador = i