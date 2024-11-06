numOne = int(input("Insert a number: "))
numTwo = int(input("Insert a number: "))
if numOne > numTwo:
    numOne, numTwo = numTwo, numOne

sum = 0

for i in range(numOne+1,numTwo):
    sum += i

print(f"The result is: {sum}")
    