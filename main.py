numOne = int(input("Insert a number: "))
numTwo = int(input("Insert a number: "))
if numOne > numTwo:
    numOne, numTwo = numTwo, numOne

sum = int() #El error no era porque no existiese, era porque no se sabía aún el tipo de la variable.

for i in range(numOne+1,numTwo):
    sum += i

print(f"The result is: {sum}")
    