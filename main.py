b = True
sum = float()
while b:
    tramo = int(input("Duracion tramo: "))
    sum += tramo
    if tramo == 0:
        b = False
print(f"Tiempo total del viaje: {sum//60:.0f}:{sum%60:.0f} horas")