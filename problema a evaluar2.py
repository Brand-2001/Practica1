calificación=int(input("ingrese una calificación: "))
if calificación<0:
    print("Calificacíón invalida")
elif calificación==100:
    print("Calificación perfecta")
elif calificación>100:
    print("Calificación inválida")
elif calificación>0 and calificación<50:
    print("insuficiente")
elif calificación>=50 and calificación<70:
    print("suficiente")
elif calificación>=70 and calificación<90:
    print("Bueno")
elif calificación>=90 and calificación<100:
    print("Excelente")