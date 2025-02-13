# class int(x, base=10), str(object='') has always been classes
# str.lower(), str.strip() are methods of the class str
# list is a class class list([iterable]), list.append()
# dict is a class too

print(type(50))
# <class 'int'>

print(type("helo, world"))
# <class 'str'>

print(type([]))
print(type(list()))
# <class 'list'> can be created by list(), identical to two empty square brackets

print(type({}))
print(type(dict()))
# <class 'dict'>