#nested loops: A loop inside a loop,
#              for every iteration of the outer loop, the inner loop will finish first.

rows = int(input("how many rows ? : "))
columns = int(input("how many columns ? : "))
symbol = input("what symbol to be used ? : ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #using the end="" will prevent the cursor to move to the next line
    print() #to make the cursor move to the next line