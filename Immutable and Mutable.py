a = 10
print(a)
print(id(a))

a = a+1
print(a)
print(id(a))

b = a
print(b)
print(id(a))
print(id(b))

c = [ 10, 'Abhi' , 20 , 30 , 40.5 ]
print(c)
print(c[0])
print(c[-1])
print(id(c))

c.append(50)
c.remove(30)
print(c)

c[0] = 90
print(c)
