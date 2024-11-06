num = int(input("Insert a number: "))
div = []
for i in range(1, num):
    if num % i == 0:
        div.append(i)
    
    if i > num/2:
        i = num

div.append(num)

print(" ".join(f"{num:3}" for num in div))