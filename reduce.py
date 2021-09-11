import functools
hello = ['h','e','l','l','o']
word = functools.reduce(lambda x, y: x+y, hello)

print(word)