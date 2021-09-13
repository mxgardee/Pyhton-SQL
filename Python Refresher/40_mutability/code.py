a = []
b = a

# Remember a and b are _names_ for the list. They both have the _same_ value.

a.append(35)  # Modify the value.

print(a)
print(b)

# We mutated (changed) the value, its names still point to the _same thing_, so it doesn't matter which name you use.

a = []
b = []

a.append(35)

print(a)
print(b)


print(id(a))
print(id(b))  # Different from id(a)

# -- immutable --

# Some values can't be changed because they don't have methods that modify the value itself.


a = 8597
b = 8597

print(id(a))
print(id(b))  # Same one

a = 8598

print(id(a))
print(
    id(b)
)  

a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"



print(id(a))
print(id(b))