#Example on Range Data Type

a = range (10)
print(type(a))
print(a)

for x in a:
	print(x)
b = range(1,20,2)
print(b)
for y in b:
	print(y)

c = range(20,1,-2)
for z in c:
	print(z)

print(a[1])
print(b[2])
print(c[3])

#None Data Type

d = 20
print(type(d))
print(d)
print(id(d))
d = None
print(type(d))
print(d)
print(id(d))

#Even if we have multiple None with different variables it will target to one none object with same id.

#Examples on Special Characters

print('Abhishek\n Things ')
print('Abhishek\t Rocks ')
print('Abhishek\r Smiles')
print('Abhishek\' Thinks')
print('Abhishek\"'' Memes')

