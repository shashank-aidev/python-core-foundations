# Experiment 1
a = 10
b = a
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))

# Experiment 2
a = 20
print("a after reassignment:", a, "id:", id(a))
print("b remains:", b, "id:", id(b))

# Experiment 3
x = 5
print("x:", x, id(x))
x = x + 1
print("x after x+1:", x, id(x))

# Experiment 4
m = 7
n = m
p = n
print(id(m), id(n), id(p))

# Experiment 5
q = 100
q = q + q
print("q:", q, id(q))

print('''python creats object to store the value with the varibale name pointing to it
varible name can be multiple like a=10, b=a, here a and b are pointing to the same value''')