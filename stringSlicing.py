#Slicing: Using indexing[start: stop: step] or slice(start, stop, step)
#start is inclusive, stop is exclusive
#Calvin -> 012345 ->(-6)(-5)(-4)(-3)(-2)(-1)
name = "Calvin"

#indexing
print(name[:3:])#Outut : Cal
print(name[::2])#Output : Cli
print(name[:-2:])#output : Calv

#slice()
sliced_obj1 = slice(0,3)
print(name[sliced_obj1])
sliced_obj2 = slice(0,-1,2)
print(name[sliced_obj2])
sliced_obj3 = slice(0,-2)
print(name[sliced_obj3])