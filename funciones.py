x = 10
if x < 30:
  print("x es menor que 30")
else:
  print("x no es menor que 30")    
  
for number in range(1,10):
    print(number)
    
for letter in "Hello":
  print(letter)
  
#funcion  
def hello(nombre="nombre"):
    print("Hello "+nombre)
hello()    

def sumar(n1, n2):
    return n1 + n2
x = sumar(2,3)    
print(x)

#funcion lambda
add = lambda n1, n2 : n1 + n2
x = add(10, 30)
print(x)
