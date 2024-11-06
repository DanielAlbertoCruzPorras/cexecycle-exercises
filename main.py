a = int(input("Altura: "))
b = int(input("Ancho: "))
for i in range(a):
    print("".join(f"* " for j in range(b)))