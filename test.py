n = int(input("Enter how many number in sequence: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

factorial = 1
for i in range(1, n + 1):
    factorial = i * factorial

print("\nFactorial: ", factorial)
