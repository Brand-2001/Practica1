numero_ing=int(input("ingrese un número: "))
if numero_ing>100:
    print("El número es mayor que 100")
elif numero_ing%2==0 and numero_ing%3==0:
    print("El  número es divisible  por 6")
elif numero_ing%2==0:
    print("El  número es divisible  por 2")
elif numero_ing%3==0:
    print("El  número es divisible  por 3")
elif numero_ing<0:
    print("El número es negativo")
else:
    print("El número no cumple ninguna condición especial")
