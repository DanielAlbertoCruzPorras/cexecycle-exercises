a = int(input("Lado: "))
msg = ""
for i in range(a-1):
    msg.join(" ")
    for j in range(a):
        msg.join("*")