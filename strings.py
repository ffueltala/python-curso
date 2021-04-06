#snake case
book_name = "Book"
#camel case
bookName = "Book"
#pascal case
BookName = "Book"

nombre, apellido = "Fernanda", "Fueltala"
print(nombre, apellido)

print(dir(nombre))

print(nombre.upper())
print(nombre.lower())
print(nombre.swapcase())
print(nombre.capitalize())
print(nombre.replace("F","Maga").upper())
print(nombre.count("a"))
print(nombre.startswith("F"))
print(nombre.endswith("F"))
print(nombre.split("a"))
print(nombre.find("a"))
print(len(nombre))
print(nombre.index("a"))
print(f"Es numerico?: {nombre.isnumeric()}")
print("Valor de la posicion 4 es {0}".format(nombre[4]))