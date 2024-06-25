x = input("Type a number: ")
x = int(x)
numbers = []
for i in range(x):
    numbers.append(i)
    print("*" * (i+1))
    i+=1