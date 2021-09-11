#Loop Control Statement : break, continue, pass
#break = terminate loop entirely
#continue = skips to the next iteration
#pass = does nothing, acts as a

#break eg.
while True:
    name = input("Please type in your name : ")
    if name != "":
        break

#continue eg.
pattern = "!@#$!@#$!@#$"

for i in pattern:
    if i == "$":
        continue
    print(i, end="")

print()

#pass eg.
for i in range(1, 21):
    if i == 10:
        pass
    else:
        print(i)