num = int(input("Insert a number: "))
div = []
for i in range(1, num):
    if num % i == 0:
        div.append(i)

div.append(num)

print(" ".join(f"{num:3}" for num in div))