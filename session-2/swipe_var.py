# swap variable values challenge

a = 5
b = 10

# 1st solution

# def swap_values(a, b):
#     return b, a
# print("Before swap: a =", a, ", b =", b)
# a, b = swap_values(a, b)
# print("After swap: a =", a, ", b =", b)


# 2nd solution

# a = 5
# b = 10

# print("Before swap: a =", a, ", b =", b)

# a, b = b, a

# print("After swap: a =", a, ", b =", b)

# 3rd solution

print("Before swap: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swap: a =", a, ", b =", b)
