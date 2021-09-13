import itertools

a1 = ["apple","banana","orange"]
a2 = ["red", "green", "blue"]
a3 = ["one", "two", "three"]

a = [a1,a2,a3]

print(list(itertools.product(*a)))
