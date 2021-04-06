x = (1,2,3)
print(x)
months = ("Enero", "Febrero", "Marzo")
print(months)
y = tuple((1,2,3))
print(y)
#arrays que no pueden modificarse
print(dir(x))
#cuando es un solo elemento no se considera tuple
z = (1)
print(type(z))

a = (1,2,3,4,5)
print(a[0])
#se elimina la tuple
del a

locations = {
    (35.122, 39.565): "Tokio",
    (65.526, 54.253) : "New York"
}

print(locations)