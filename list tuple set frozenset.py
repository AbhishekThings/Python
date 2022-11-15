#Examples on List Data Types
a = [ 10 , 20 , 10 , 40 , 'Abhi']
print(type(a))
print(a)
a.append(50)
print(a)
a.remove(10)
print(a)
print(a[0])
print(a[-1])
b = [ 10, 20, 30 , 20 , 'Shek' ]
print(type(b))
print(b)


#Examples on Tupple Data Type

c = ( 10 , 20 , 30 , 'Abhishek' )
print(type(c))
print(c)
print(c[0])
print(c[-1])
print(c)

#we cannot use append or remove function in tuple because tuple is an immutable data type we can only read the values and indexing is allowed..

#Examples on Set Data type

d = { 10 , 20 , 30 , 10 , 'AbhiRam' , 50 , 200 }
print(type(d))
print(d)

#As Ordering is not important in Set DT we cant use indexing but we can add and remove elements in set

d.add(60)
print(d)
d.remove(10)
print(d)


#Examples on Frozenset

#as frozenset is a function we cant give values directly so we need to create a set and call frozenset function.

e ={ 'Abhi' , ' Ram ' , 200 , 400 , 500 , 200 }
print(type(e))
print(e)
f= frozenset(e)
print(type(f))
print(f)


#Examples on Dict 

g = { 100:'Abhi' , 200:'Ram' , 300: 300 }
print(type(g))
print(g)
