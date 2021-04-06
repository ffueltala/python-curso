demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]
#list solo soporta un elemento
numbers_list = list((1, 2, 3, 4))
print(numbers_list)
#una lista de rangos
r = list(range(0,10))
print(r)

print(len(colors))
print(colors[2])
print("green" in colors)
#colors.append(["violet","yellow"])
#colors.extend(["violet","yellow"])
#colors.insert(3, "violet")
#colors.remove("green")
#colors.pop()
#colors.clear()
#colors.sort()
#ordenar de manera inversa
#colors.sort(reverse=True)
print(colors.index("blue"))
print(colors.count("blue"))
#print(colors)