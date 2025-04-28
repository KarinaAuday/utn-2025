num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

match operacion:
    case '+':
        print(f"Resultado: {num1 + num2}")
    case '-':
        print(f"Resultado: {num1 - num2}")
    case '*':
        print(f"Resultado: {num1 * num2}")
    case '/':
        if num2 == 0:
            print("ERROR")
        else:
            print(f"Resultado: {num1 / num2}")
    case _:
        print("Operación inválida")
