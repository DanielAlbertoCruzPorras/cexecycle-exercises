a = int(input("Altura: "))

for i in range(1,a+1):
    print("".join(f"*" for j in range(i)))