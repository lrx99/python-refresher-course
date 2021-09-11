#set is a collection of unindexed, unordered and no dupluicated values
#faster to print out a set compared to a list

char = {"A", "B", "C", "4"}
int  = {"1", "2", "3", "A"}

rub = int.union(char)#a new set created
print(rub)

for i in rub:
    print(i)

print(char.difference(int)) #shows what int do not have that char have
print(char.intersection(int)) #shows the only similar element between both set